from robot.hummingbird import Hummingbird
from robot.tasks import Tasks
from robot.hummingbird_dual_motor_driver import HummingbirdDualMotorDriver

from battle_bot_driving import driving
from battle_bot_extras import extras
from battle_bot_weapons import weapons
from xbox_joystick import XboxJoystick

hummingbird = HummingbirdDualMotorDriver("A")

joystick = XboxJoystick().connect()

print("Battlebot Ready")

tasks = Tasks()

tasks.create_task(driving(hummingbird, joystick))
tasks.create_task(weapons(hummingbird, joystick))
tasks.create_task(extras(hummingbird, joystick))

tasks.run()
