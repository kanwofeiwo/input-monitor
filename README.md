# input-monitor
![项目横幅](./OIP-C.jpeg)
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

[简体中文](README.zh-CN.md)

Smart input source switcher for different focusing windows on **Linux-ibus**

A Python script that automatically switches input source between English and Rime (or other input sources) based on the currently focused window on Linux systems. This tool helps users seamlessly switch between different input methods without manual intervention, and includes smart features like temporary switching with long-press Shift.

## Table of Contents
- [Background](#background)
- [Features](#features)
- [Install](#install)
- [Usage](#usage)
- [Configuration](#configuration)
- [Maintainers](#maintainers)
- [Contributing](#contributing)
- [License](#license)

## Background
Input-monitor was created to solve the common problem of manually switching input sources when working with different applications on Linux. Many users need to frequently switch between English and other input methods (like Rime for Chinese input) depending on the application they're using. This tool automates that process by monitoring window focus changes and automatically switching input sources accordingly.

The script uses Python with keyboard monitoring capabilities to detect focus changes and execute input source switching commands seamlessly in the background.

## Features

- **Automatic Window-based Switching**: Automatically switches input methods based on window titles
- **Default Fallback**: When no keywords match, automatically falls back to Rime input method
- **Long-press Shift Temporary Switch**: Hold left Shift for 200ms to temporarily switch from Rime to English, release to switch back
- **Hotkey Controls**: Easy-to-use keyboard shortcuts for controlling the application
- **Real-time Monitoring**: Monitors active windows every second for responsive switching
- **Configurable Rules**: Easily customize window title keywords and corresponding input methods

## Install

This project uses [Python 3](https://python.org) and requires several Python packages. Make sure you have Python installed locally.

### Prerequisites

Make sure you have the following installed:
- Linux operating system
- Python 3.x
- IBus input method framework
- `xdotool` (for window detection)

Install system dependencies:
```sh
# On Ubuntu/Debian
$ sudo apt install xdotool ibus

# On Fedora/RHEL
$ sudo dnf install xdotool ibus

# On Arch Linux
$ sudo pacman -S xdotool ibus
```

Clone the repository:
```sh
$ git clone https://github.com/kanwofeiwo/input-monitor.git
$ cd input-monitor
```

Install required Python dependencies:
```sh
$ pip install pynput
```

Note: `subprocess`, `time`, and `threading` are built-in Python modules and don't need separate installation.

## Usage

Run the input monitor script:
```sh
$ python input-monitor.py
```

### Keyboard Shortcuts

The application supports the following keyboard shortcuts:

- **Z+X**: Toggle monitoring on/off
- **Z+X+C**: Quit the application
- **Long-press Left Shift (200ms+)**: Temporarily switch from Rime to English input method (only when current method is Rime)

### Default Behavior

- **Window-based switching**: Input method switches based on predefined window title keywords
- **Default fallback**: When no keywords match the current window title, the system defaults to Rime input method
- **Temporary switching**: Long-press left Shift to temporarily use English input while in Rime mode

## Configuration

### Window-Input Method Mapping

Modify the `keyword_to_engine` dictionary in the main section (around line 110):

```python
keyword_to_engine = {
    "peter": "xkb:us::eng",  # Switch to English when window title contains 'peter'
    "edge": "rime",          # Switch to Rime when window title contains 'edge'
    "/": "xkb:us::eng",      # Switch to English for paths
    "vim": "xkb:us::eng",    # Switch to English for Vim
    ".py": "xkb:us::eng",    # Switch to English for Python files
    "QQ": "rime",            # Switch to Rime for QQ
    ".tex": "rime",          # Switch to Rime for LaTeX files
    ".v": "xkb:us::eng"      # Switch to English for Verilog files
}
```

### Default Input Method

Change the default input method (around line 114):
```python
default_engine = "rime"  # Change this to your preferred default
```

### Keyboard Shortcuts

Modify the key combinations in the `on_press` function (around line 45):
```python
# Current: Z+X for toggle, Z+X+C for quit
if 'z' in current_keys and 'x' in current_keys:
    # Modify these key combinations as needed
```

### Long-press Timing

Adjust the long-press detection time in the `on_press` function (around line 55):
```python
shift_timer = threading.Timer(0.2, on_shift_long_press)  # Change 0.2 to desired seconds
```

### System Requirements

- Linux operating system with X11
- Python 3.x
- IBus input method framework
- `xdotool` for window title detection
- Rime input method or other input sources you want to switch between

## Troubleshooting

### Common Issues

1. **"xdotool not found"**: Install xdotool using your package manager
2. **"ibus not configured"**: Make sure IBus is running and properly configured
3. **Input methods not switching**: Verify your input method engine names using `ibus engine`
4. **Permission issues**: Make sure the script has permission to monitor keyboard input

### Checking Available Input Methods

List available IBus engines:
```sh
$ ibus list-engine
```

Get current active engine:
```sh
$ ibus engine
```

## Contributing

PRs accepted.

Small note: If editing the README, please conform to the [standard-readme](https://github.com/RichardLitt/standard-readme) specification.

## License

[MIT](LICENSE) © kanwofeiwo
