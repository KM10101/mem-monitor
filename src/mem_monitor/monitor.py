#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/23/周六 17:41
# @Author  : qli
import sys
import tracemalloc
import time
import threading
import logging
import os
import atexit
from typing import Dict, Any

from loguru import logger

from mem_monitor.config import get_config


class MemoryMonitor:
    _instance = None
    _initialized = False
    _lock = threading.Lock()  # 添加线程锁

    def __new__(cls, config=None):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(MemoryMonitor, cls).__new__(cls)
        return cls._instance

    def __init__(self, config: Dict[str, Any] = None):
        """
        初始化内存监控器

        Args:
            config: 配置字典
        """
        if self._initialized:
            return

        self.config = config or {}
        self.running = False
        self.monitor_thread = None
        self.baseline_snapshot = None

        # 设置日志
        pid = os.getpid()

        # 日志格式
        log_format = (
            "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
            "<level>{level: <8}</level> | "
            "<cyan>PID {extra[pid]}</cyan> | "
            "<level>{message}</level>"
        )

        # 文件输出
        log_file = self.config.get('log_file', 'memory_monitor.log')

        logger.add(
            log_file,
            format=log_format,
            level=self.config.get('log_level', 'INFO'),
            rotation=self.config.get('log_rotation', '100 MB'),
            retention=self.config.get('log_retention', '1 week'),
            backtrace=True,
            diagnose=True,
            filter=lambda record: record["extra"].get("pid") == pid
        )

        # 为当前进程绑定 PID
        self.logger = logger.bind(pid=pid)

        # 设置 tracemalloc
        tracemalloc.start(self.config.get('stack_depth', 10))

        # 注册退出时的清理函数
        atexit.register(self.stop)

        self._initialized = True
        self.logger.info(f"内存监控器初始化完成 (PID: {pid})")

    def take_snapshot(self):
        """
        获取内存快照并分析
        """
        snapshot = tracemalloc.take_snapshot()
        top_stats = snapshot.statistics('lineno')

        pid = os.getpid()
        top_n = self.config.get('top_n', 5)
        self.logger.info("=" * 60)
        self.logger.info(f"进程 {pid} 内存使用情况 Top {top_n}")

        for i, stat in enumerate(top_stats[:top_n]):
            self.logger.info(f"#{i + 1}: {stat}")
            for line in stat.traceback.format():
                self.logger.info(f"    {line}")

        # 如果有比较基准，显示与基准的差异
        if self.baseline_snapshot:
            diff_stats = snapshot.compare_to(self.baseline_snapshot, 'lineno')
            self.logger.info("=" * 60)
            self.logger.info(f"进程 {pid} 与基准相比的内存变化 Top {top_n} ")

            for i, stat in enumerate(diff_stats[:top_n]):
                self.logger.info(f"#{i+1}: {stat}")
                for line in stat.traceback.format():
                    self.logger.info(f"    {line}")

    def set_baseline(self):
        """
        设置基准快照
        """
        self.baseline_snapshot = tracemalloc.take_snapshot()
        pid = os.getpid()
        self.logger.info(f"进程 {pid} 已设置内存使用基准")

    def monitor_loop(self):
        """
        监控循环
        """
        self.set_baseline()

        while self.running:
            self.take_snapshot()
            time.sleep(self.config.get('interval', 30))

    def start(self):
        """
        启动监控
        """
        if self.running:
            return

        self.running = True
        self.monitor_thread = threading.Thread(target=self.monitor_loop)
        self.monitor_thread.daemon = True
        self.monitor_thread.start()

        pid = os.getpid()
        interval = self.config.get('interval', 30)
        self.logger.info(f"进程 {pid} 内存监控已启动，间隔: {interval}秒")

    def stop(self):
        """
        停止监控
        """
        if not self.running:
            return

        self.running = False
        if self.monitor_thread:
            self.monitor_thread.join(timeout=1.0)

        pid = os.getpid()
        self.logger.info(f"进程 {pid} 内存监控已停止")


def init_monitor(config: Dict[str, Any] = None):
    """
    初始化内存监控器

    Args:
        config: 配置字典
    """
    # 初始化内存监控
    try:
        if not config:
            config = get_config()
        monitor = MemoryMonitor(config)
        monitor.start()
        print("内存监控已启动")
    except Exception as e:
        print(f"启动内存监控失败: {e}")