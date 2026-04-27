from robot.hummingbird import Hummingbird
from time import sleep

hummingbird = Hummingbird()

for i in range(10):
    # IN1 triled Red
    # IN2 triles Green
    # IN3 triled Red
    # IN4 triled Green

    # IN1=HIGH, IN2=LOW: Motor A spins forward.
    # IN1=LOW, IN2=HIGH: Motor A spins backward.
    # IN1=IN2: Motor A stops (brake).
    # IN3=HIGH, IN4=LOW: Motor B spins forward.
    # IN3=LOW, IN4=HIGH: Motor B spins backward.
    # IN3=IN4: Motor B stops (brake). 

    speed = 75
    sleep_amount = 0.5

    # motor A forward
    hummingbird.tri_led(1, speed, 0, 0)
    sleep(sleep_amount)

    # motor A backward
    hummingbird.tri_led(1, 0, speed, 0)
    sleep(sleep_amount)

    # motor B forward
    hummingbird.tri_led(2, speed, 0, 0)
    sleep(sleep_amount)

    # motor B backward
    hummingbird.tri_led(2, 0, speed, 0)
    sleep(sleep_amount)

    hummingbird.tri_led(1, speed, speed, 0)
    hummingbird.tri_led(2, speed, speed, 0)

    # both forward
    hummingbird.tri_led(1, speed, 0, 0)
    hummingbird.tri_led(2, speed, 0, 0)
    sleep(5.0)

    # both backward
    hummingbird.tri_led(1, 0, speed, 0)
    hummingbird.tri_led(2, 0, speed, 0)
    sleep(5.0)

    hummingbird.tri_led(1, 0, 0, 0)
    hummingbird.tri_led(2, 0, 0, 0)
    sleep(sleep_amount)


