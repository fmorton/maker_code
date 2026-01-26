from robot.tasks import Tasks
from robot.hummingbird_dual_motor_driver import HummingbirdDualMotorDriver
from robot.xbox_joystick import XboxJoystick

from battle_bot_driving import driving
from battle_bot_event_manager import event_manager
from battle_bot_extras import extras
from battle_bot_weapons import weapons

import asyncio

hummingbird = HummingbirdDualMotorDriver("A")

joystick = XboxJoystick().connect()

print("Battlebot Ready")

driving_queue = asyncio.Queue()
weapons_queue = asyncio.Queue()
extras_queue = asyncio.Queue()

tasks = Tasks()

tasks.create_task(event_manager(joystick, driving_queue, weapons_queue, extras_queue))
tasks.create_task(driving(hummingbird, joystick, driving_queue))
tasks.create_task(weapons(hummingbird, joystick, weapons_queue))
tasks.create_task(extras(hummingbird, joystick, extras_queue))

tasks.run()
