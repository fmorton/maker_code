from battle_bot_driving import driving
from battle_bot_events import events
from battle_bot_extras import extras
from battle_bot_weapons import weapons
from robot.tasks import Tasks
from robot.hummingbird_dual_motor_driver import HummingbirdDualMotorDriver
from robot.xbox_controller import XboxController


hummingbird = HummingbirdDualMotorDriver("A")
controller = XboxController().connect()

print("Battlebot Ready")

tasks = Tasks()

tasks.create_task(events(controller, True))
tasks.create_task(driving(hummingbird, controller))
tasks.create_task(weapons(hummingbird, controller))
tasks.create_task(extras(hummingbird, controller))

tasks.run()
