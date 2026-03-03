from robot.hummingbird_dual_motor_driver import HummingbirdDualMotorDriver
from robot.xbox_joystick import XboxJoystick
from time import sleep


def robot(joystick):
    # --------------------------------------------------------------------------------------------------------------------------
    #  exit
    # --------------------------------------------------------------------------------------------------------------------------
    if joystick.state.button_down_milliseconds(XboxJoystick.BUTTON_XBOX):
        return False

    # --------------------------------------------------------------------------------------------------------------------------
    #  driving
    # --------------------------------------------------------------------------------------------------------------------------
    left_speed = right_speed = round(-joystick.state.left_y() * 100, 2) + 0.0

    # add turning

    hummingbird.move(left_speed, right_speed)

    # --------------------------------------------------------------------------------------------------------------------------
    #  weapons
    # --------------------------------------------------------------------------------------------------------------------------
    left_weapon = joystick.state.left_trigger() * 100.0
    right_weapon = joystick.state.right_trigger() * 100.0

    # --------------------------------------------------------------------------------------------------------------------------
    #  state string
    # --------------------------------------------------------------------------------------------------------------------------
    extra_state_string = ""
    extra_state_string += f"{left_weapon:8.2f}"
    extra_state_string += f"{right_weapon:8.2f}"
    extra_state_string += f"{left_speed:8.2f}"
    extra_state_string += f"{right_speed:8.2f}"

    joystick.state.print_state_string(extra_state_string)

    sleep(XboxJoystick.EVENT_LOOP_DELAY)

    return True


hummingbird = HummingbirdDualMotorDriver("A")
joystick = XboxJoystick().connect()

print("Battlebot Ready")

joystick.run(robot)
