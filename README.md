# input-monitor

![项目横幅](./OIP-C.jpeg)

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

[简体中文](README.zh-CN.md)

> Switch input source for different focusing windows on **Linux-ibus**

A Python script that automatically switches input source between English and Rime (or other input sources) based on the currently focused window on Linux systems. This tool helps users seamlessly switch between different input methods without manual intervention.

## Table of Contents

- [Background](#background)
- [Install](#install)
- [Usage](#usage)
- [Maintainers](#maintainers)
- [Contributing](#contributing)
- [License](#license)

## Background

Input-monitor was created to solve the common problem of manually switching input sources when working with different applications on Linux. Many users need to frequently switch between English and other input methods (like Rime for Chinese input) depending on the application they're using. This tool automates that process by monitoring window focus changes and automatically switching input sources accordingly.

The script uses Python with keyboard monitoring capabilities to detect focus changes and execute input source switching commands seamlessly in the background.

## Install

This project uses [Python 3](https://python.org) and requires several Python packages. Make sure you have Python installed locally.

Clone the repository:

```sh
$ git clone https://github.com/kanwofeiwo/input-monitor.git
$ cd input-monitor
```

Install required dependencies:

```sh
$ pip install pynput
```

Note: `subprocess` and `time` are built-in Python modules and don't need separate installation.

## Usage

Run the input monitor script:

```sh
$ python input-monitor.py
```

### Keyboard Shortcuts

The application supports the following keyboard shortcuts:

- **z+x**: Suspend/continue monitoring
- **z+x+c**: Quit the application

### Configuration

Before running the script, you may need to customize it for your specific setup:

1. **Change window-input mapping** (line 85): 
   ```python
   if __name__ == "__main__":
       # Modify the window-input source mappings here
   ```

2. **Change keyboard shortcuts** (line 52):
   ```python
   def on_press(key):
       # Modify the key combinations here
   ```

### System Requirements

- Linux operating system
- Python 3.x
- Input method framework (such as IBus, Fcitx, etc.)
- Rime input method or other input sources you want to switch between


## Contributing

PRs accepted.

Small note: If editing the README, please conform to the [standard-readme](https://github.com/RichardLitt/standard-readme) specification.

## License

[MIT](LICENSE) © kanwofeiwo
