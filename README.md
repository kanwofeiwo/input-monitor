# input-monitor

![Project Banner](./OIP-C.jpeg)
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)

[中文](README.zh-CN.md)

Intelligent input method switching tool for **Linux** & **Windows**

A cross-platform Python script that automatically switches between English and Chinese input methods (Rime, Pinyin, etc.) based on the currently focused window. This tool helps users seamlessly switch between different input methods without manual intervention, featuring smart functionality like long-press Shift for temporary switching.

## Table of Contents
- [Background](#background)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Platform Support](#platform-support)
- [Troubleshooting](#troubleshooting)
- [Maintainers](#maintainers)
- [Contributing](#contributing)
- [License](#license)

## Background

Input-monitor aims to solve the common problem of manually switching input methods when using different applications. Many users need to frequently switch between English and other input methods (such as Chinese Rime or native system input methods) depending on the application they're using. This tool automates this process by monitoring window focus changes and automatically switching input methods accordingly.

The script uses Python's keyboard monitoring capabilities to detect focus changes and seamlessly executes input method switching commands in the background across all major operating systems.

## Features

- **Cross-platform support**: Works on Linux (IBus), Windows
- **Window-based automatic switching**: Automatically switches input methods based on window titles
- **Default fallback mechanism**: Automatically falls back to your preferred input method when no keywords match
- **Long-press Shift temporary switching**: Long-press left Shift for 200ms to temporarily switch from Chinese to English, returns when released, making special symbol input faster
- **Hotkey control**: Easy-to-use keyboard shortcuts to control the application
- **Real-time monitoring**: Monitors active window every 1 second in a loop

## Installation

This project uses [Python 3](https://python.org) and requires several Python packages. Make sure you have Python 3.6+ installed locally.

### System Requirements

#### Linux
```sh
# Ubuntu/Debian systems
$ sudo apt install xdotool ibus python3-pip

# Fedora/RHEL systems
$ sudo dnf install xdotool ibus python3-pip

# Arch Linux systems
$ sudo pacman -S xdotool ibus python
```

#### Windows
- Windows 10/11
- Python 3.6+

### Installation Steps

Clone the repository:
```sh
$ git clone https://github.com/kanwofeiwo/input-monitor.git
$ cd input-monitor
```

Install required Python dependencies:

**Linux:**
```sh
$ pip install pynput
```

**Windows:**
```sh
$ pip install pynput pywin32 psutil pyautogui
```

## Usage

### Running the Script

**Linux:**
```sh
$ python input-monitor.py
```

**Windows:**
```sh
$ python windows-input-monitor.py
```

### Initial Setup

#### Windows
1. Run the script as administrator
2. Adjust the `INPUT_METHODS` dictionary in the script according to your installed input methods
3. Test the input method switching functionality manually first

### Keyboard Shortcuts

The application supports the following keyboard shortcuts on all platforms:

- **Z+X**: Toggle monitoring on/off
- **Z+X+C**: Exit the application
- **Long-press left Shift (200ms+)**: Temporarily switch to English input method, restore original input method when released

### Default Behavior

- **Window-based switching**: Switches input methods based on predefined window title keywords
- **Default fallback**: Uses the configured default input method when no keywords match the current window title
- **Temporary switching**: Long-press left Shift to temporarily use English input while in Chinese mode
- **Smart switching**: Only switches when necessary to avoid interruption

## Configuration

### Window-Input Method Mapping

Modify the `keyword_to_engine` dictionary in the respective platform scripts:

**Linux:**
```python
keyword_to_engine = {
    "peter": "xkb:us::eng",  # Switch to English when window title contains 'peter'
    "edge": "rime",          # Switch to Rime when window title contains 'edge'
    "vim": "xkb:us::eng",    # Use English for Vim
    ".py": "xkb:us::eng",    # Use English for Python files
    "QQ": "rime",            # Use Rime for QQ
    ".tex": "rime",          # Use Rime for LaTeX files
}
```

**Windows:**
```python
keyword_to_engine = {
    "notepad": "en",         # Use English for Notepad
    "visual studio": "en",   # Use English for VS
    "qq": "zh",              # Use Chinese for QQ
    "wechat": "zh",          # Use Chinese for WeChat
    ".py": "en",             # Use English for Python files
}
```

### Default Input Method

Change the default input method in each script:
```python
default_engine = "rime"  # Linux
default_engine = "zh"    # Windows
```

### Long-press Time Adjustment

Adjust the long-press detection time:
```python
shift_timer = threading.Timer(0.2, on_shift_long_press)  # Change 0.2 to desired seconds
```

### Custom Hotkeys

Modify the key combinations in the `on_press` function:
```python
# Current: Z+X toggles functionality, Z+X+C exits
if 'z' in current_keys and 'x' in current_keys:
    # Modify these key combinations as needed
```

## Troubleshooting

### Linux Issues
1. **"xdotool not found"**: `sudo apt install xdotool`
2. **"ibus not configured"**: Ensure IBus is running: `ibus-daemon -drx`
3. **Input method not switching**: Check available engines: `ibus list-engine`

### Windows Issues
1. **Script not working**: Run as administrator
2. **Input method not switching**: Adjust `INPUT_METHODS` identifiers
3. **Permission errors**: Check User Account Control settings
4. **Hotkeys not working**: Install pyautogui: `pip install pyautogui`

### Debugging

Enable verbose logging by adding debug prints:
```python
print(f"[DEBUG] Current window: {title}")
print(f"[DEBUG] Matched engine: {matched_engine}")
```

Check available input methods:
```sh
# Linux
$ ibus list-engine

# Windows - Check in Language settings
```

## Development

### Project Structure
```
input-monitor/
├── input-monitor.py          # Linux version (original)
├── windows-input-monitor.py  # Windows version
├── macos-input-monitor.py    # macOS version
├── README.md                 # English documentation
├── README.zh-CN.md           # Chinese documentation
└── LICENSE                   # MIT License
```

## Contributing

Contributions are welcome! Here's how you can help:

1. **Bug reports**: Open issues with detailed information
2. **Feature requests**: Suggest new features or improvements
3. **Platform support**: Help add support for new platforms
4. **Documentation**: Improve documentation and examples
5. **Testing**: Test on different systems and configurations

PRs are welcome. When editing the README, please follow the [standard-readme](https://github.com/RichardLitt/standard-readme) specification.

## Maintainers

[@kanwofeiwo](https://github.com/kanwofeiwo)

## License

[MIT](LICENSE) © kanwofeiwo

---

⭐ If this project helped you, please consider giving it a star!

🐛 Found a bug? Please [report it](../../issues/new)
