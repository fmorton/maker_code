import random

from robot.hummingbird import Hummingbird
from time import sleep

BRIGHTNESS = 2

hummingbird_1 = Hummingbird("A")  # TSF
hummingbird_2 = Hummingbird("B")  # STP


def random_color():
    red = random.randint(0, BRIGHTNESS)
    green = random.randint(0, BRIGHTNESS)
    blue = random.randint(0, BRIGHTNESS)

    return red, green, blue


def set_white(hummingbird_1, hummingbird_2, tri_led_1, tri_led_2, tri_led_3, tri_led_4):
    hummingbird_1.tri_led(1, tri_led_1, tri_led_1, tri_led_1)
    hummingbird_1.tri_led(2, tri_led_2, tri_led_2, tri_led_2)
    hummingbird_2.tri_led(1, tri_led_3, tri_led_3, tri_led_3)
    hummingbird_2.tri_led(2, tri_led_4, tri_led_4, tri_led_4)

    sleep(0.05)


def set_random_color(hummingbird, port):
    red, green, blue = random_color()

    hummingbird.tri_led(port, red, green, blue)

    sleep(0.1)


while True:
    for _ in range(5):
        set_white(hummingbird_1, hummingbird_2, BRIGHTNESS, 0, 0, 0)
        set_white(hummingbird_1, hummingbird_2, 0, BRIGHTNESS, 0, 0)
        set_white(hummingbird_1, hummingbird_2, 0, 0, BRIGHTNESS, 0)
        set_white(hummingbird_1, hummingbird_2, 0, 0, 0, BRIGHTNESS)

    # sleep(random.uniform(0.4, 0.9))
    for _ in range(10):
        set_random_color(hummingbird_1, 1)
        set_random_color(hummingbird_1, 2)
        set_random_color(hummingbird_2, 1)
        set_random_color(hummingbird_2, 2)
