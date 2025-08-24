# 内存监控工具 (mem-monitor)

一个用于监控Python应用程序内存使用情况的轻量级工具。

## 安装

```shell
uv pip install https://github.com/KM10101/mem-monitor.git
```

## 配置

### 环境变量配置（推荐）

通过环境变量指定配置文件路径：

```shell
export MEM_MONITOR_CONFIG=/path/to/config.yaml
```

### 配置文件示例

```yaml
# 监控配置
interval: 30           # 监控间隔（秒）
stack_depth: 5         # 堆栈跟踪深度
top_n: 10              # 显示前N个内存占用最多的代码段

# 日志配置
log_level: INFO        # 日志级别: DEBUG, INFO, WARNING, ERROR, CRITICAL
log_file: memory.log   # 日志文件路径
```

## 使用方法

### 方法一：使用配置文件

在项目初始化代码中添加以下代码：

```python
from mem_monitor.monitor import init_monitor
init_monitor()
```

### 方法二：直接传入配置参数

```python
from mem_monitor.monitor import init_monitor

config = {
    "interval": 30,
    "stack_depth": 5,
    "top_n": 10,
    "log_level": "INFO",
    "log_file": "memory.log"
}

init_monitor(config)
```

## 配置参数说明

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| interval | int | 30 | 监控间隔（秒） |
| stack_depth | int | 5 | 堆栈跟踪深度 |
| top_n | int | 10 | 显示前N个内存占用最多的代码段 |
| log_level | string | "INFO" | 日志级别: DEBUG, INFO, WARNING, ERROR, CRITICAL |
| log_file | string | "memory.log" | 日志文件路径 |


## 输出日志示例

```text
2025-08-23 20:19:08.733 | INFO     | PID 98960 | 进程 98960 内存使用情况 Top 10
2025-08-23 20:19:08.733 | INFO     | PID 98960 | #1: E:\projects\python\test-fastapi\app.py:136: size=25.0 MiB, count=2, average=12.5 MiB
2025-08-23 20:19:08.734 | INFO     | PID 98960 |       File "E:\projects\python\test-fastapi\app.py", line 136
2025-08-23 20:19:08.735 | INFO     | PID 98960 |         memory_block = [0] * (size_bytes // 8)  # 每个整数约8字节
2025-08-23 20:19:08.736 | INFO     | PID 98960 | #2: D:\Python\Python312\Lib\linecache.py:142: size=870 KiB, count=9320, average=96 B
2025-08-23 20:19:08.736 | INFO     | PID 98960 |       File "D:\Python\Python312\Lib\linecache.py", line 142
2025-08-23 20:19:08.737 | INFO     | PID 98960 |         lines = fp.readlines()
2025-08-23 20:19:08.738 | INFO     | PID 98960 | #3: <frozen importlib._bootstrap_external>:757: size=183 KiB, count=1495, average=125 B
2025-08-23 20:19:08.739 | INFO     | PID 98960 |       File "<frozen importlib._bootstrap_external>", line 757
2025-08-23 20:19:08.739 | INFO     | PID 98960 | #4: D:\Python\Python312\Lib\asyncio\proactor_events.py:191: size=64.1 KiB, count=2, average=32.0 KiB
2025-08-23 20:19:08.740 | INFO     | PID 98960 |       File "D:\Python\Python312\Lib\asyncio\proactor_events.py", line 191
2025-08-23 20:19:08.741 | INFO     | PID 98960 |         self._data = bytearray(buffer_size)
2025-08-23 20:19:08.741 | INFO     | PID 98960 | #5: D:\Python\Python312\Lib\tracemalloc.py:193: size=62.7 KiB, count=1338, average=48 B
2025-08-23 20:19:08.742 | INFO     | PID 98960 |       File "D:\Python\Python312\Lib\tracemalloc.py", line 193
2025-08-23 20:19:08.743 | INFO     | PID 98960 |         self._frames = tuple(reversed(frames))
2025-08-23 20:19:08.744 | INFO     | PID 98960 | #6: D:\Python\Python312\Lib\tracemalloc.py:115: size=46.0 KiB, count=589, average=80 B
2025-08-23 20:19:08.745 | INFO     | PID 98960 |       File "D:\Python\Python312\Lib\tracemalloc.py", line 115
2025-08-23 20:19:08.745 | INFO     | PID 98960 |         return (abs(self.size_diff), self.size,
2025-08-23 20:19:08.746 | INFO     | PID 98960 | #7: D:\Python\Python312\Lib\tracemalloc.py:67: size=36.7 KiB, count=587, average=64 B
2025-08-23 20:19:08.747 | INFO     | PID 98960 |       File "D:\Python\Python312\Lib\tracemalloc.py", line 67
2025-08-23 20:19:08.748 | INFO     | PID 98960 |         return (self.size, self.count, self.traceback)
2025-08-23 20:19:08.749 | INFO     | PID 98960 | #8: <frozen abc>:106: size=35.9 KiB, count=132, average=278 B
2025-08-23 20:19:08.750 | INFO     | PID 98960 |       File "<frozen abc>", line 106
2025-08-23 20:19:08.750 | INFO     | PID 98960 | #9: <frozen importlib._bootstrap>:488: size=13.9 KiB, count=90, average=158 B
2025-08-23 20:19:08.751 | INFO     | PID 98960 |       File "<frozen importlib._bootstrap>", line 488
2025-08-23 20:19:08.752 | INFO     | PID 98960 | #10: E:\projects\python\test-fastapi\.venv\Lib\site-packages\loguru\_logger.py:2003: size=6850 B, count=137, average=50 B
2025-08-23 20:19:08.752 | INFO     | PID 98960 |       File "E:\projects\python\test-fastapi\.venv\Lib\site-packages\loguru\_logger.py", line 2003
2025-08-23 20:19:08.754 | INFO     | PID 98960 |         elapsed = current_datetime - start_time
2025-08-23 20:19:08.858 | INFO     | PID 98960 | ============================================================
2025-08-23 20:19:08.858 | INFO     | PID 98960 | 进程 98960 与基准相比的内存变化 Top 10 
2025-08-23 20:19:08.859 | INFO     | PID 98960 | #1: E:\projects\python\test-fastapi\app.py:136: size=25.0 MiB (+25.0 MiB), count=2 (+2), average=12.5 MiB
2025-08-23 20:19:08.860 | INFO     | PID 98960 |       File "E:\projects\python\test-fastapi\app.py", line 136
2025-08-23 20:19:08.860 | INFO     | PID 98960 |         memory_block = [0] * (size_bytes // 8)  # 每个整数约8字节
2025-08-23 20:19:08.862 | INFO     | PID 98960 | #2: D:\Python\Python312\Lib\linecache.py:142: size=870 KiB (+870 KiB), count=9320 (+9320), average=96 B
2025-08-23 20:19:08.863 | INFO     | PID 98960 |       File "D:\Python\Python312\Lib\linecache.py", line 142
2025-08-23 20:19:08.863 | INFO     | PID 98960 |         lines = fp.readlines()
2025-08-23 20:19:08.864 | INFO     | PID 98960 | #3: <frozen importlib._bootstrap_external>:757: size=183 KiB (+183 KiB), count=1495 (+1495), average=125 B
2025-08-23 20:19:08.865 | INFO     | PID 98960 |       File "<frozen importlib._bootstrap_external>", line 757
2025-08-23 20:19:08.866 | INFO     | PID 98960 | #4: D:\Python\Python312\Lib\asyncio\proactor_events.py:191: size=64.1 KiB (+64.1 KiB), count=2 (+2), average=32.0 KiB
2025-08-23 20:19:08.867 | INFO     | PID 98960 |       File "D:\Python\Python312\Lib\asyncio\proactor_events.py", line 191
2025-08-23 20:19:08.867 | INFO     | PID 98960 |         self._data = bytearray(buffer_size)
2025-08-23 20:19:08.869 | INFO     | PID 98960 | #5: D:\Python\Python312\Lib\tracemalloc.py:193: size=62.7 KiB (+62.7 KiB), count=1338 (+1338), average=48 B
2025-08-23 20:19:08.870 | INFO     | PID 98960 |       File "D:\Python\Python312\Lib\tracemalloc.py", line 193
2025-08-23 20:19:08.871 | INFO     | PID 98960 |         self._frames = tuple(reversed(frames))
2025-08-23 20:19:08.871 | INFO     | PID 98960 | #6: D:\Python\Python312\Lib\tracemalloc.py:115: size=46.0 KiB (+46.0 KiB), count=589 (+589), average=80 B
2025-08-23 20:19:08.872 | INFO     | PID 98960 |       File "D:\Python\Python312\Lib\tracemalloc.py", line 115
2025-08-23 20:19:08.873 | INFO     | PID 98960 |         return (abs(self.size_diff), self.size,
2025-08-23 20:19:08.874 | INFO     | PID 98960 | #7: D:\Python\Python312\Lib\tracemalloc.py:67: size=36.7 KiB (+36.7 KiB), count=587 (+587), average=64 B
2025-08-23 20:19:08.875 | INFO     | PID 98960 |       File "D:\Python\Python312\Lib\tracemalloc.py", line 67
2025-08-23 20:19:08.875 | INFO     | PID 98960 |         return (self.size, self.count, self.traceback)
2025-08-23 20:19:08.876 | INFO     | PID 98960 | #8: <frozen abc>:106: size=35.9 KiB (+35.9 KiB), count=132 (+132), average=278 B
2025-08-23 20:19:08.877 | INFO     | PID 98960 |       File "<frozen abc>", line 106
2025-08-23 20:19:08.878 | INFO     | PID 98960 | #9: <frozen importlib._bootstrap>:488: size=13.9 KiB (+13.9 KiB), count=90 (+90), average=158 B
2025-08-23 20:19:08.879 | INFO     | PID 98960 |       File "<frozen importlib._bootstrap>", line 488
2025-08-23 20:19:08.880 | INFO     | PID 98960 | #10: E:\projects\python\test-fastapi\.venv\Lib\site-packages\loguru\_logger.py:2003: size=6850 B (+6750 B), count=137 (+135), average=50 B
2025-08-23 20:19:08.881 | INFO     | PID 98960 |       File "E:\projects\python\test-fastapi\.venv\Lib\site-packages\loguru\_logger.py", line 2003
2025-08-23 20:19:08.881 | INFO     | PID 98960 |         elapsed = current_datetime - start_time
2025-08-23 20:19:38.972 | INFO     | PID 98960 | ============================================================
```