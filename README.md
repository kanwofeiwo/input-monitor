# input-monitor
switch input source for different  focusing windows on linux
use pyscript to switch input source between English and rime( or other input source for you)


Install:

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

