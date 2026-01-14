import random

from robot.hummingbird import Hummingbird
from time import sleep

LIGHT_CUTOFF_LEVEL = 7


def light_sensor_not_covered():
    print("NOT COVERED")
    bird.position_servo(1, 76)
    bird.position_servo(2, 75)


def light_sensor_covered():
    print("COVERED")
    bird.position_servo(1, random.randint(55, 95))
    sleep(random.uniform(0.1, 0.75))

    bird.position_servo(2, random.randint(55, 95))
    sleep(random.uniform(0.1, 0.75))

    sleep(0.10)


bird = Hummingbird("A")

while True:
    if bird.light(1) < LIGHT_CUTOFF_LEVEL:
        light_sensor_covered()
    else:
        light_sensor_not_covered()
