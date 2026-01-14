from pynput import keyboard
import queue
import time


class Keyboard:
    def process(self, key):
        self.keyboard_queue.put(key)

    def on_press(self, input_key):
        try:
            key = input_key.char
        except AttributeError:
            key = str(input_key)

            if key == "Key.space":
                key = " "

        self.process(key)

    def __init__(self):
        self.listener = keyboard.Listener(on_press=self.on_press, suppress=True)

        self.listener.start()

        self.keyboard_queue = queue.Queue()

    def is_key_available(self):
        return self.keyboard_queue.qsize() > 0

    def key(self):
        if self.is_key_available():
            return self.keyboard_queue.get()

        return None


keyboard = Keyboard()

while True:
    while (key := keyboard.key()) is not None:
        print(
            "Program running...",
            keyboard.keyboard_queue,
            "size:",
            keyboard.keyboard_queue.qsize(),
            "......",
            key,
        )

    # time.sleep(0.25)
