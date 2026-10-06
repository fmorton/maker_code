from robot.hummingbird import Hummingbird
from time import sleep

hummingbird = Hummingbird("A")

hummingbird.led(2, 70)
hummingbird.position_servo(4, 0)

sleep(1)

hummingbird.position_servo(4, 180)

sleep(1)

hummingbird.led(2, 0)
hummingbird.position_servo(4, 90)

