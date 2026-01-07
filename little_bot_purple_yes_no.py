import random

from robot.hummingbird import Hummingbird
from time import sleep

SERVO_UP_DOWN = 1
SERVO_SIDE_TO_SIDE = 2

hummingbird = Hummingbird("A")

while True:
    if hummingbird.light(1) < 10:
        hummingbird.position_servo(SERVO_UP_DOWN, 60)
        hummingbird.position_servo(SERVO_SIDE_TO_SIDE, 70)

        while hummingbird.light(1) < 10:
            sleep(0.1)

        answer = random.random()
        print(answer)

        if answer <= 0.4:
            for _ in range(5):
                hummingbird.position_servo(SERVO_UP_DOWN, 50)
                sleep(0.2)
                hummingbird.position_servo(SERVO_UP_DOWN, 70)
                sleep(0.2)
        elif answer <= 0.8:
            for _ in range(5):
                hummingbird.position_servo(SERVO_SIDE_TO_SIDE, 60)
                sleep(0.2)
                hummingbird.position_servo(SERVO_SIDE_TO_SIDE, 80)
                sleep(0.2)
        else:
                sleep(2)

    hummingbird.position_servo(SERVO_UP_DOWN, random.randint(60, 100))
    hummingbird.position_servo(SERVO_SIDE_TO_SIDE, random.randint(50, 95))

    sleep(random.uniform(0.4, 0.9))
