#input-monitor#
switch input source for different  focusing windows** on linux**
use pyscript to switch input source between English and rime( or other input source for you)


Install:
# Input Monitor (输入法监视器)

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

一个 Linux 下根据当前聚焦窗口自动切换输入法的 Python 脚本。

本工具旨在解决在 Linux 环境下，需要在不同应用程序（如代码编辑器、浏览器、聊天工具）之间频繁切换输入法（例如，英文和 Rime 中文输入法）的痛点。它能监视当前窗口焦点，并根据预设规则自动切换到合适的输入法，提升工作效率。

## 内容列表

- [背景](#背景)
- [安装](#安装)
- [使用说明](#使用说明)
- [配置](#配置)
- [如何贡献](#如何贡献)
- [使用许可](#使用许可)

---

## 背景

在 Linux 系统中，不同的应用程序可能需要使用不同的输入法。例如，在编写代码时通常使用英文输入法，而在聊天或撰写文档时则可能需要中文或其他语言的输入法。手动切换不仅繁琐，还容易打断工作流程。`Input Monitor` 通过自动化这一过程，让您可以更专注于当前任务。

---

## 安装

**1. 先决条件**

* **Linux 环境**: 本脚本专为 Linux 设计。
* **Python 3**: 确保您的系统已安装 Python 3。
* **Git**: 用于克隆仓库。
* **pip**: 用于安装 Python 依赖库。

**2. 克隆仓库**

```sh
git clone [https://github.com/kanwofeiwo/input-monitor.git](https://github.com/kanwofeiwo/input-monitor.git)
cd input-monitor
git clone https://github.com/kanwofeiwo/input-monitor.git


Required third-party libraries:

pip install subprocess

pip install time

pip install pynput


Using instruction:

shortcut"z+x":suspend/continue

shortcut"z+x+c":quit


Change details for you

1.change windows-input in line 85:if __name__ == "__main__":

2.change shortcut in line 52:def on_press(key):

