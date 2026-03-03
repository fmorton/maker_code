from battle_bot_processes_driving import driving
from battle_bot_processes_event_manager import event_manager
from battle_bot_processes_extras import extras
from battle_bot_processes_weapons import weapons
from robot.hummingbird_dual_motor_driver import HummingbirdDualMotorDriver
from robot.processes import Processes
from robot.xbox_joystick import XboxJoystick


hummingbird = HummingbirdDualMotorDriver("A")
joystick = XboxJoystick().connect()

print("Battlebot Ready")

processes = Processes()

processes.create_process(event_manager, (joystick,))
processes.create_process(driving, (hummingbird, joystick))
processes.create_process(weapons, (hummingbird, joystick))
processes.create_process(extras, (hummingbird, joystick))

processes.run()