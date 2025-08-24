#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/23/周六 17:39
# @Author  : qli
import os

import yaml
from typing import Dict, Any


def load_config(config_path: str) -> Dict[str, Any]:
    """
    加载 YAML 配置文件

    Args:
        config_path: 配置文件路径

    Returns:
        配置字典
    """
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    return config



def get_config():
    """
    从环境变量获取配置路径并加载配置

    Returns:
        配置字典
    """
    config_path = os.environ.get('MEM_MONITOR_CONFIG')
    if not config_path:
        raise ValueError("环境变量 MEM_MONITOR_CONFIG 未设置")

    return load_config(config_path)