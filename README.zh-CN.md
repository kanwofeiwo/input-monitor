# input-monitor
![项目横幅](./OIP-C.jpeg)
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)

[English](README.md)

适用于 **Linux**&**Windows** 的智能输入法切换工具

基于当前焦点窗口自动在英文和中文输入法（Rime、拼音等）之间切换的跨平台 Python 脚本。该工具帮助用户无需手动干预即可在不同输入法之间无缝切换，具有长按 Shift 临时切换等智能功能。

## 目录
- [背景](#背景)
- [功能特性](#功能特性)
- [安装](#安装)
- [使用方法](#使用方法)
- [配置说明](#配置说明)
- [平台支持](#平台支持)
- [故障排除](#故障排除)
- [维护者](#维护者)
- [贡献](#贡献)
- [许可证](#许可证)

## 背景
Input-monitor 旨在解决在使用不同应用程序时手动切换输入法的常见问题。许多用户需要根据所使用的应用程序频繁在英文和其他输入法（如中文的 Rime 或系统原生输入法）之间切换。该工具通过监控窗口焦点变化并相应地自动切换输入法来实现这一过程的自动化。

该脚本使用 Python 的键盘监控功能来检测焦点变化，并在所有主要操作系统的后台无缝执行输入法切换命令。

## 功能特性

- ** 跨平台支持**：适用于 Linux (IBus)、Windows
- ** 基于窗口的自动切换**：根据窗口标题自动切换输入法
- ** 默认回退机制**：当没有关键字匹配时，自动回退到您偏好的输入法
- ** 长按 Shift 临时切换**：长按左 Shift 200ms 从中文临时切换到英文，释放后切回,使得输入特殊符号更快捷
- ** 热键控制**：易用的键盘快捷键控制应用程序
- ** 实时监控**：每1秒循环监控活动窗口

## 安装

本项目使用 [Python 3](https://python.org) 并需要多个 Python 包。确保本地安装了 Python 3.6+。

### 系统要求

#### Linux
```sh
# Ubuntu/Debian 系统
$ sudo apt install xdotool ibus python3-pip

# Fedora/RHEL 系统
$ sudo dnf install xdotool ibus python3-pip

# Arch Linux 系统
$ sudo pacman -S xdotool ibus python
```

#### Windows
- Windows 10/11
- Python 3.6+


### 安装步骤

克隆仓库：
```sh
$ git clone https://github.com/kanwofeiwo/input-monitor.git
$ cd input-monitor
```

安装所需的 Python 依赖：

**Linux：**
```sh
$ pip install pynput
```

**Windows：**
```sh
$ pip install pynput pywin32 psutil pyautogui
```


## 使用方法

### 运行脚本

**Linux：**
```sh
$ python input-monitor.py
```

**Windows：**
```sh
$ python windows-input-monitor.py
```


### 首次设置

#### Windows
1. 以管理员身份运行脚本
2. 根据已安装的输入法调整脚本中的 `INPUT_METHODS` 字典
3. 先手动测试输入法切换功能


### 键盘快捷键

应用程序在所有平台上支持以下键盘快捷键：

- **Z+X**：切换监控开/关
- **Z+X+C**：退出应用程序
- **长按左 Shift（200ms+）**：临时切换到英文输入法,松开后恢复原输入法

### 默认行为

- **基于窗口的切换**：根据预定义的窗口标题关键字切换输入法
- **默认回退**：当没有关键字匹配当前窗口标题时，使用配置的默认输入法
- **临时切换**：长按左 Shift 在中文模式下临时使用英文输入
- **智能切换**：仅在必要时切换，避免中断

## 配置说明

### 窗口-输入法映射

修改各平台脚本中的 `keyword_to_engine` 字典：

**Linux：**
```python
keyword_to_engine = {
    "peter": "xkb:us::eng",  # 窗口标题包含 'peter' 时切换到英文
    "edge": "rime",          # 窗口标题包含 'edge' 时切换到 Rime
    "vim": "xkb:us::eng",    # Vim 使用英文
    ".py": "xkb:us::eng",    # Python 文件使用英文
    "QQ": "rime",            # QQ 使用 Rime
    ".tex": "rime",          # LaTeX 文件使用 Rime
}
```

**Windows：**
```python
keyword_to_engine = {
    "notepad": "en",         # 记事本使用英文
    "visual studio": "en",   # VS 使用英文
    "qq": "zh",              # QQ 使用中文
    "wechat": "zh",          # 微信使用中文
    ".py": "en",             # Python 文件使用英文
}
```


### 默认输入法

在各脚本中更改默认输入法：
```python
default_engine = "rime"  # Linux
default_engine = "zh"    # Windows
```

### 长按时间调整

调整长按检测时间：
```python
shift_timer = threading.Timer(0.2, on_shift_long_press)  # 将 0.2 改为所需秒数
```

### 自定义热键

修改 `on_press` 函数中的组合键：
```python
# 当前：Z+X 切换功能，Z+X+C 退出
if 'z' in current_keys and 'x' in current_keys:
    # 根据需要修改这些组合键
```


## 故障排除

### Linux 问题
1. **"xdotool not found"**：`sudo apt install xdotool`
2. **"ibus not configured"**：确保 IBus 正在运行：`ibus-daemon -drx`
3. **输入法不切换**：检查可用引擎：`ibus list-engine`

### Windows 问题
1. **脚本不工作**：以管理员身份运行
2. **输入法不切换**：调整 `INPUT_METHODS` 标识符
3. **权限错误**：检查用户账户控制设置
4. **热键不工作**：安装 pyautogui：`pip install pyautogui`



### 调试

通过添加调试打印启用详细日志：
```python
print(f"[DEBUG] 当前窗口: {title}")
print(f"[DEBUG] 匹配的引擎: {matched_engine}")
```

检查可用的输入法：
```sh
# Linux
$ ibus list-engine

# Windows - 在语言设置中检查

```

## 开发

### 项目结构
```
input-monitor/
├── input-monitor.py          # Linux 版本（原版）
├── windows-input-monitor.py  # Windows 版本
├── macos-input-monitor.py    # macOS 版本
├── README.md                 # 英文文档
├── README.zh-CN.md           # 中文文档
└── LICENSE                   # MIT 许可证
```


## 贡献

欢迎贡献！以下是您可以帮助的方式：

1. **错误报告**：使用详细信息开启 issue
2. **功能请求**：建议新功能或改进  
3. **平台支持**：帮助添加新平台支持
4. **文档**：改进文档和示例
5. **测试**：在不同系统和配置上测试

欢迎提交 PR。编辑 README 时请遵循 [standard-readme](https://github.com/RichardLitt/standard-readme) 规范。

## 维护者

[@kanwofeiwo](https://github.com/kanwofeiwo)

## 许可证

[MIT](LICENSE) © kanwofeiwo

---

⭐ 如果这个项目帮助了您，请考虑给它一个星标！


🐛 发现了错误？请[报告它](../../issues/new)
