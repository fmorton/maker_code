from robot.hummingbird_dual_motor_driver import HummingbirdDualMotorDriver
from time import sleep

hummingbird = HummingbirdDualMotorDriver("A")

left_speed = 0
right_speed = 30

hummingbird.move(left_speed, right_speed)

sleep(.5)

hummingbird.move(0, 0)
