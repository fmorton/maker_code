from pynput import keyboard

from robot.constant import Constant
from time import sleep


def on_press(key):
    try:
        # Handle alphanumeric keys
        print("Alphanumeric key {0} pressed".format(key.char))
    except AttributeError:
        # Handle special keys
        print("Special key {0} pressed".format(key))
        # if key == keyboard.Key.up:
        if key == Constant.KEY_UP:
            print("Up key specifically detected!")
        elif key == keyboard.Key.down:
            print("Down key specifically detected!")
        elif key == keyboard.Key.left:
            print("Left key specifically detected!")
        elif key == keyboard.Key.right:
            print("Right key specifically detected!")


def on_release(key):
    print("{0} released".format(key))
    # Stop listener when Esc is pressed
    if key == keyboard.Key.esc:
        return False


# Collect events until released
print("starting up")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    # listener.join()s
    pass

while True:
    print("Running...")
    sleep(1)
