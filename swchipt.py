import subprocess
import time
from pynput import keyboard

# 全局变量：用于控制切换功能和终止程序
is_switching_enabled = True
terminate_script = False
current_keys = set()  # 记录当前按下的按键


'''def get_active_window_title():
    """获取当前活动窗口的标题"""
    try:
        result = subprocess.run(['xdotool', 'getactivewindow', 'getwindowname'],
                                stdout=subprocess.PIPE, text=True)
        return result.stdout.strip() if result.stdout.strip() else "No active window detected."
    except FileNotFoundError:
        return "Error: xdotool is not installed. Please install it using 'sudo apt install xdotool'."
    except Exception as e:
        return f"An error occurred: {e}"'''


def get_active_window_title():
    """获取当前活动窗口的标题"""
    try:
        result = subprocess.run(['xdotool', 'getactivewindow', 'getwindowname'],
                                stdout=subprocess.PIPE, text=True)
        title = result.stdout.strip() if result.stdout.strip() else "No active window detected."
        #print(f"当前活动窗口: {title}")
        return title
    except FileNotFoundError:
        error_msg = "Error: xdotool is not installed. Please install it using 'sudo apt install xdotool'."
        print(error_msg)
        return error_msg
    except Exception as e:
        error_msg = f"An error occurred: {e}"
        print(error_msg)
        return error_msg


def switch_input_method(engine):
    """切换输入法到指定的引擎"""
    try:
        subprocess.run(['ibus', 'engine', engine], check=True)
        print(f">>>[{time.strftime('%Y-%m-%d %H:%M:%S')}] Input method switched to '{engine}'")
    except FileNotFoundError:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Error: ibus is not installed or not configured properly. Please install/configure ibus.")
    except subprocess.CalledProcessError as e:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Error switching input method: {e}")


def on_press(key):
    """处理按键按下事件"""
    global is_switching_enabled, terminate_script
    try:
        if hasattr(key, 'char') and key.char:  # 检查是否为字符按键
            current_keys.add(key.char)
        elif hasattr(key, 'name'):  # 检查特殊按键
            current_keys.add(key.name)

        # 检查组合键 Z+X
        if 'z' in current_keys and 'x' in current_keys:
            if 'c' in current_keys:  # 检查 Z+X+C
                terminate_script = True
                print(">>> Termination signal received. Exiting...")
            else:  # 仅 Z+X 切换功能状态
                is_switching_enabled = not is_switching_enabled
                state = "enabled" if is_switching_enabled else "disabled"
                print(f">>> Switching function {state}.")
    except AttributeError:
        pass


def on_release(key):
    """处理按键释放事件"""
    try:
        if hasattr(key, 'char') and key.char:
            current_keys.discard(key.char)
        elif hasattr(key, 'name'):
            current_keys.discard(key.name)
    except AttributeError:
        pass


if __name__ == "__main__":
    keyword_to_engine = {
        "peter": "xkb:us::eng",  # 当标题包含 'peter' 时切换到 'xkb:us::eng'
        "edge": "rime",          # 当标题包含 'edge' 时切换到 'rime'
        "/": "xkb:us::eng",
        "vim": "xkb:us::eng",
        #" - ": "xkb:us::eng",
        ".py": "xkb:us::eng",
        "QQ": "rime",
        ".tex":"rime",
        ".v":"xkb:us::eng"
    }

    print("Monitoring active window title every 2 seconds...\nPress Z+X to toggle switching, Z+X+C to terminate.")

    # 启动键盘监听器
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()

    last_keyword = None  # 记录上一次匹配的关键字

    try:
        while not terminate_script:  # 终止条件
            if is_switching_enabled:
                title = get_active_window_title()
                #print(f" {title}")

                # 根据关键字匹配切换输入法
                current_keyword = None  # 当前匹配的关键字
                current_engine = None   # 当前匹配的输入法引擎
                for keyword, engine in keyword_to_engine.items():
                    if keyword in title.lower():  # 不区分大小写匹配
                        current_keyword = keyword
                        current_engine = engine
                        break

                # 如果关键字不同于上一次，才切换输入法
                if current_keyword != last_keyword:
                    if current_engine:
                        switch_input_method(current_engine)
                    last_keyword = current_keyword

            time.sleep(1)  # 每隔 2 秒检查一次
    except KeyboardInterrupt:
        print("Monitoring stopped. Goodbye!")
    finally:
        listener.stop()