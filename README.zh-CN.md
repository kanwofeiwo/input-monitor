# input-monitor

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

[English](README.md)

> 在 Linux 系统中为不同的焦点窗口切换输入法

一个 Python 脚本，可以根据 Linux 系统中当前聚焦的窗口自动在英语和 Rime（或其他输入法）之间切换输入源。该工具帮助用户无需手动干预即可在不同输入法之间无缝切换。

## 目录

- [背景](#背景)
- [安装](#安装)
- [使用](#使用)
- [接口](#接口)
- [维护者](#维护者)
- [贡献](#贡献)
- [许可证](#许可证)

## 背景

Input-monitor 的创建是为了解决在 Linux 上使用不同应用程序时手动切换输入源的常见问题。许多用户需要根据正在使用的应用程序频繁地在英语和其他输入法（如用于中文输入的 Rime）之间切换。该工具通过监控窗口焦点变化并相应地自动切换输入源来自动化这一过程。

该脚本使用具有键盘监控功能的 Python 来检测焦点变化，并在后台无缝执行输入源切换命令。

## 安装

该项目使用 [Python 3](https://python.org) 并需要几个 Python 包。请确保您已在本地安装 Python。

克隆仓库：

```sh
$ git clone https://github.com/kanwofeiwo/input-monitor.git
$ cd input-monitor
```

安装所需依赖：

```sh
$ pip install pynput
```

注意：`subprocess` 和 `time` 是 Python 内置模块，无需单独安装。

## 使用

运行输入监控脚本：

```sh
$ python input-monitor.py
```

### 键盘快捷键

应用程序支持以下键盘快捷键：

- **z+x**：暂停/继续监控
- **z+x+c**：退出应用程序

### 配置

在运行脚本之前，您可能需要根据您的具体设置进行自定义：

1. **更改窗口-输入法映射**（第85行）： 
   ```python
   if __name__ == "__main__":
       # 在此处修改窗口-输入源映射
   ```

2. **更改键盘快捷键**（第52行）：
   ```python
   def on_press(key):
       # 在此处修改组合键
   ```

### 系统要求

- Linux 操作系统
- Python 3.x
- 输入法框架（如 IBus、Fcitx 等）
- Rime 输入法或您想要切换的其他输入源

## 接口

这是一个独立脚本，不提供 API 接口。主要功能通过以下方式处理：

- 窗口焦点检测
- 输入源切换
- 键盘快捷键处理

该脚本监控系统事件并自动响应，无需直接 API 调用。

## 维护者

[@kanwofeiwo](https://github.com/kanwofeiwo)

## 贡献

欢迎提交 PR。

小提示：如果编辑 README，请遵循 [standard-readme](https://github.com/RichardLitt/standard-readme) 规范。

## 许可证

[MIT](LICENSE) © kanwofeiwo
