import random

from robot.finch import Finch
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

    finch.motors(left_speed, right_speed)

    # ------------------------------------------------------------------------------------------------------------------
    #  weapons
    # ------------------------------------------------------------------------------------------------------------------
    left_weapon = controller.state.left_trigger() * 100.0
    right_weapon = controller.state.right_trigger() * 100.0

    finch.beak(max(left_weapon, right_weapon), 15, 0)
    finch.tail(1, left_weapon, 5, 0)
    finch.tail(4, right_weapon, 5, 0)

    if (
        controller.state.button_down_milliseconds(XboxController.BUTTON_LEFT_BUMPER)
        > 0.25
    ):
        red = random.randint(0, 100)
        green = random.randint(0, 100)
        blue = random.randint(0, 100)

        finch.tail(2, red, blue, green)
        finch.tail(3, red, blue, green)
    else:
        finch.tail(2, 0, 0, 0)
        finch.tail(3, 0, 0, 0)

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


finch = Finch("A")
controller = XboxController().connect()

print("Ready")

controller.run(robot)
