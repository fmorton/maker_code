from robot.hummingbird import Hummingbird
from robot.hummingbird_l298n_dual_motor_driver import HummingbirdL298nDualMotorDriver
from time import sleep

hummingbird = Hummingbird()
hummingbird_driver = HummingbirdL298nDualMotorDriver(hummingbird)

hummingbird_driver.move_left_motor(25)
sleep(1.0)

hummingbird_driver.move_left_motor(-25)
sleep(1.0)

hummingbird_driver.stop()

hummingbird_driver.move_right_motor(25)
sleep(1.0)

hummingbird_driver.move_right_motor(-25)
sleep(1.0)

hummingbird_driver.stop()
