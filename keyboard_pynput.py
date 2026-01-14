from pynput import keyboard
import time


def on_press(key):
    try:
        print(f"Key pressed: {key.char}", "class", key.__class__.__name__)
    except AttributeError:
        print(f"Special key pressed: {key}", "class", key.__class__.__name__)


listener = keyboard.Listener(on_press=on_press, suppress=True)
listener.start()

while True:
    print("Program running...")

    time.sleep(1)
