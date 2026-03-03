from battle_bot_processes_driving import driving
from battle_bot_processes_event_manager import event_manager
from battle_bot_processes_extras import extras
from battle_bot_processes_weapons import weapons
from multiprocessing import Queue
from robot.hummingbird_dual_motor_driver import HummingbirdDualMotorDriver
from robot.processes import Processes
from robot.xbox_joystick import XboxJoystick

if __name__ == "__main__":
    hummingbird = HummingbirdDualMotorDriver("A")

    event_queue = Queue()

    processes = Processes()

    processes.create_process(event_manager, (event_queue, False))
    processes.create_process(driving, (hummingbird, event_queue))
    #processes.create_process(weapons, (hummingbird, joystick))
    #processes.create_process(extras, (hummingbird, joystick))

    processes.run()