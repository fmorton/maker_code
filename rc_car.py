from robot.hummingbird import Hummingbird
from time import sleep

hummingbird = Hummingbird("A")

hummingbird.tri_led(1, 0, 0, 0)
hummingbird.tri_led(2, 0, 0, 0)

STEERING_VOLTAGE = 50
STEERING_PORT = 2

while True:
    hummingbird.tri_led(STEERING_PORT, STEERING_VOLTAGE, 0, 0)
    sleep(2)
    hummingbird.tri_led(STEERING_PORT, 0, STEERING_VOLTAGE, 0)
    sleep(2)
    hummingbird.tri_led(2, 0, 0, 0)
    sleep(2)
