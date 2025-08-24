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