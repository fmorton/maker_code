from battle_bot_driving import driving
from battle_bot_event_manager import event_manager
from battle_bot_extras import extras
from battle_bot_weapons import weapons
from robot.hummingbird_dual_motor_driver import HummingbirdDualMotorDriver
from robot.processes import Processes
from robot.xbox_controller import XboxController


hummingbird = HummingbirdDualMotorDriver("A")
controller = XboxController().connect()

print("Battlebot Ready")

processes = Processes()

processes.create_process(event_manager, (controller,))
processes.create_process(driving, (hummingbird, controller))
processes.create_process(weapons, (hummingbird, controller))
processes.create_process(extras, (hummingbird, controller))

processes.run()
