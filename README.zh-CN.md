# input-monitor
![项目横幅](./OIP-C.jpeg)
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

[English](README.md)

基于活动窗口的 **Linux-ibus** 智能输入法切换工具

一个 Python 脚本，根据当前聚焦的窗口在 Linux 系统上自动在英文和 Rime（或其他输入法）之间切换输入源。此工具帮助用户无需手动干预即可在不同输入法之间无缝切换，并包含长按 Shift 临时切换等智能功能。

## 目录
- [背景](#背景)
- [功能特性](#功能特性)
- [安装](#安装)
- [使用](#使用)
- [配置](#配置)
- [维护者](#维护者)
- [贡献](#贡献)
- [许可证](#许可证)

## 背景
Input-monitor 的创建是为了解决在 Linux 上使用不同应用程序时需要手动切换输入源的常见问题。许多用户需要根据正在使用的应用程序频繁地在英文和其他输入法（如用于中文输入的 Rime）之间切换。此工具通过监控窗口焦点变化并相应地自动切换输入源来自动化这一过程。

该脚本使用具有键盘监控功能的 Python 来检测焦点变化并在后台无缝执行输入源切换命令。

## 功能特性

- **基于窗口的自动切换**: 根据窗口标题自动切换输入法
- **默认回退机制**: 当没有关键字匹配时，自动回退到 Rime 输入法
- **长按 Shift 临时切换**: 长按左 Shift 键 200ms 从 Rime 临时切换到英文，松开后切换回来
- **热键控制**: 易于使用的键盘快捷键来控制应用程序
- **实时监控**: 每秒监控活动窗口以实现响应式切换
- **可配置规则**: 轻松自定义窗口标题关键字和对应的输入法

## 安装

此项目使用 [Python 3](https://python.org) 并需要几个 Python 包。确保您已在本地安装 Python。

### 前置条件

确保您已安装以下组件：
- Linux 操作系统
- Python 3.x
- IBus 输入法框架
- `xdotool`（用于窗口检测）

安装系统依赖：
```sh
# 在 Ubuntu/Debian 上
$ sudo apt install xdotool ibus

# 在 Fedora/RHEL 上
$ sudo dnf install xdotool ibus

# 在 Arch Linux 上
$ sudo pacman -S xdotool ibus
```

克隆仓库：
```sh
$ git clone https://github.com/kanwofeiwo/input-monitor.git
$ cd input-monitor
```

安装所需的 Python 依赖：
```sh
$ pip install pynput
```

注意：`subprocess`、`time` 和 `threading` 是 Python 内置模块，无需单独安装。

## 使用

运行输入法监控脚本：
```sh
$ python input-monitor.py
```

### 键盘快捷键

应用程序支持以下键盘快捷键：

- **Z+X**: 切换监控开/关
- **Z+X+C**: 退出应用程序
- **长按左 Shift（200ms+）**: 从 Rime 临时切换到英文输入法（仅当前输入法为 Rime 时）

### 默认行为

- **基于窗口的切换**: 输入法根据预定义的窗口标题关键字切换
- **默认回退**: 当没有关键字匹配当前窗口标题时，系统默认使用 Rime 输入法
- **临时切换**: 在 Rime 模式下长按左 Shift 键临时使用英文输入

## 配置

### 窗口-输入法映射

修改主要部分中的 `keyword_to_engine` 字典（约第 110 行）：

```python
keyword_to_engine = {
    "peter": "xkb:us::eng",  # 窗口标题包含 'peter' 时切换到英文
    "edge": "rime",          # 窗口标题包含 'edge' 时切换到 Rime
    "/": "xkb:us::eng",      # 路径时切换到英文
    "vim": "xkb:us::eng",    # Vim 时切换到英文
    ".py": "xkb:us::eng",    # Python 文件时切换到英文
    "QQ": "rime",            # QQ 时切换到 Rime
    ".tex": "rime",          # LaTeX 文件时切换到 Rime
    ".v": "xkb:us::eng"      # Verilog 文件时切换到英文
}
```

### 默认输入法

更改默认输入法（约第 114 行）：
```python
default_engine = "rime"  # 将此更改为您偏好的默认输入法
```

### 键盘快捷键

在 `on_press` 函数中修改按键组合（约第 45 行）：
```python
# 当前：Z+X 切换，Z+X+C 退出
if 'z' in current_keys and 'x' in current_keys:
    # 根据需要修改这些按键组合
```

### 长按时间

在 `on_press` 函数中调整长按检测时间（约第 55 行）：
```python
shift_timer = threading.Timer(0.2, on_shift_long_press)  # 将 0.2 更改为所需的秒数
```

### 系统要求

- 带有 X11 的 Linux 操作系统
- Python 3.x
- IBus 输入法框架
- 用于窗口标题检测的 `xdotool`
- Rime 输入法或您想要切换的其他输入源

## 故障排除

### 常见问题

1. **"找不到 xdotool"**: 使用包管理器安装 xdotool
2. **"ibus 未配置"**: 确保 IBus 正在运行并正确配置
3. **输入法未切换**: 使用 `ibus engine` 验证您的输入法引擎名称
4. **权限问题**: 确保脚本有权限监控键盘输入

### 检查可用的输入法

列出可用的 IBus 引擎：
```sh
$ ibus list-engine
```

获取当前活动的引擎：
```sh
$ ibus engine
```

## 贡献

欢迎 PR。

小提示：如果编辑 README，请遵守 [standard-readme](https://github.com/RichardLitt/standard-readme) 规范。

## 许可证

[MIT](LICENSE) © kanwofeiwo
