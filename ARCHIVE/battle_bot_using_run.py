from robot.hummingbird_dual_motor_driver import HummingbirdDualMotorDriver
from robot.xbox_controller import XboxController
from time import sleep


def robot(controller):
    # ------------------------------------------------------------------------------------------------------------------
    #  exit
    # ------------------------------------------------------------------------------------------------------------------
    if controller.state.button_down_milliseconds(XboxController.BUTTON_XBOX):
        return False

    # ------------------------------------------------------------------------------------------------------------------
    #  driving
    # ------------------------------------------------------------------------------------------------------------------
    FACTOR = 0.75

    left_speed = right_speed = round(-controller.state.left_y() * 100, 2) + 0.0

    speed_multiplier = 1.0 - (abs(controller.state.right_x()) * FACTOR)

    if controller.state.right_x() >= 0.0:
        right_speed = right_speed * speed_multiplier  # turn right (slower right wheel)
    else:
        left_speed = left_speed * speed_multiplier  # turn left (slower left wheel)

    hummingbird.move(left_speed, right_speed)

    # ------------------------------------------------------------------------------------------------------------------
    #  weapons
    # ------------------------------------------------------------------------------------------------------------------
    left_weapon = controller.state.left_trigger() * 100.0
    right_weapon = controller.state.right_trigger() * 100.0

    # ------------------------------------------------------------------------------------------------------------------
    #  state string
    # ------------------------------------------------------------------------------------------------------------------
    extra_state_string = ""
    extra_state_string += f"{left_weapon:8.2f}"
    extra_state_string += f"{right_weapon:8.2f}"
    extra_state_string += f"{left_speed:8.2f}"
    extra_state_string += f"{right_speed:8.2f}"
    extra_state_string += f"{speed_multiplier:8.2f}"

    controller.state.print_state_string(extra_state_string)

    sleep(XboxController.EVENT_LOOP_DELAY)

    return True


hummingbird = HummingbirdDualMotorDriver("A")
controller = XboxController().connect()

controller.run(robot)
