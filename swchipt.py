import subprocess
import time
import threading
from pynput import keyboard

# 全局变量：用于控制切换功能和终止程序
is_switching_enabled = True
terminate_script = False
current_keys = set()  # 记录当前按下的按键

# 长按Shift相关变量
shift_press_time = None  # Shift按下的时间
shift_long_press_detected = False  # 是否检测到长按
original_input_method = None  # 记录长按前的原始输入法
shift_timer = None  # 计时器对象


def get_active_window_title():
    """获取当前活动窗口的标题"""
    try:
        result = subprocess.run(['xdotool', 'getactivewindow', 'getwindowname'],
                                stdout=subprocess.PIPE, text=True)
        title = result.stdout.strip() if result.stdout.strip() else "No active window detected."
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


def get_current_input_method():
    """获取当前输入法引擎"""
    try:
        result = subprocess.run(['ibus', 'engine'], stdout=subprocess.PIPE, text=True)
        return result.stdout.strip() if result.stdout.strip() else None
    except (FileNotFoundError, subprocess.CalledProcessError):
        return None


def on_shift_long_press():
    """处理Shift长按事件"""
    global shift_long_press_detected, original_input_method
    
    if not is_switching_enabled:
        return
        
    # 获取当前输入法
    current_method = get_current_input_method()
    if current_method == "rime":
        shift_long_press_detected = True
        original_input_method = current_method
        switch_input_method("xkb:us::eng")
        print(f">>> Shift long press detected, temporarily switched from rime to xkb:us::eng")


def on_press(key):
    """处理按键按下事件"""
    global is_switching_enabled, terminate_script, shift_press_time, shift_timer
    
    try:
        # 处理Shift左键长按检测
        if key == keyboard.Key.shift_l:
            shift_press_time = time.time()
            # 设置200ms后的定时器
            if shift_timer:
                shift_timer.cancel()
            shift_timer = threading.Timer(0.2, on_shift_long_press)
            shift_timer.start()
        
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
    global shift_press_time, shift_long_press_detected, original_input_method, shift_timer
    
    try:
        # 处理Shift左键释放
        if key == keyboard.Key.shift_l:
            # 取消定时器
            if shift_timer:
                shift_timer.cancel()
                shift_timer = None
            
            # 如果检测到了长按，恢复原输入法
            if shift_long_press_detected and original_input_method:
                switch_input_method(original_input_method)
                print(f">>> Shift released, switched back to {original_input_method}")
                shift_long_press_detected = False
                original_input_method = None
            
            shift_press_time = None
        
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
        ".py": "xkb:us::eng",
        "QQ": "rime",
        ".tex": "rime",
        ".v": "xkb:us::eng"
    }
    
    # 默认输入法（未匹配到关键字时使用）
    default_engine = "rime"

    print("Monitoring active window title every 1 second...\nPress Z+X to toggle switching, Z+X+C to terminate.")
    print(f"Default input method (when no keywords match): {default_engine}")
    print("Long press left Shift (200ms+) to temporarily switch from rime to English input method.")

    # 启动键盘监听器
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()

    last_engine = None  # 记录上一次使用的输入法引擎

    try:
        while not terminate_script:  # 终止条件
            if is_switching_enabled:
                title = get_active_window_title()

                # 根据关键字匹配切换输入法
                matched_engine = None   # 当前匹配的输入法引擎
                for keyword, engine in keyword_to_engine.items():
                    if keyword in title.lower():  # 不区分大小写匹配
                        matched_engine = engine
                        break

                # 如果没有匹配到关键字，使用默认输入法
                if matched_engine is None:
                    matched_engine = default_engine

                # 只有当需要切换的输入法与上一次不同时才切换
                if matched_engine != last_engine:
                    switch_input_method(matched_engine)
                    last_engine = matched_engine

            time.sleep(1)  # 每隔 1 秒检查一次
    except KeyboardInterrupt:
        print("Monitoring stopped. Goodbye!")
    finally:
        # 清理定时器
        if shift_timer:
            shift_timer.cancel()
        listener.stop()
