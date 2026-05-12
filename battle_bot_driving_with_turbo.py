from robot.hummingbird_l298n_dual_motor_driver import HummingbirdL298nDualMotorDriver
from robot.tasks import Tasks
from robot.xbox_joystick import XboxJoystick
from time import sleep


async def driving(hummingbird, joystick):
    running = True
    turbo_mode = False

    hummingbird.led(1, 0)

    hummingbird_driver = HummingbirdL298nDualMotorDriver(hummingbird)

    while running:
        # ----------------------------------------------------------------------------------------------------------------------
        #  set turbo mode based on "Y" button toggle
        # ----------------------------------------------------------------------------------------------------------------------
        if joystick.state.button_down_milliseconds(XboxJoystick.BUTTON_A):
            turbo_mode = not turbo_mode

            hummingbird.led(1, turbo_mode * 15)

        # ----------------------------------------------------------------------------------------------------------------------
        #  driving
        # ----------------------------------------------------------------------------------------------------------------------
        FACTOR = 0.75

        left_speed = right_speed = round(-joystick.state.left_y() * 100, 2) + 0.0

        direction = joystick.state.right_x()
        speed_multiplier = 1.0 - (abs(direction) * FACTOR)

        if turbo_mode:
            VOLTAGE_FACTOR = 0.25

            if direction == 0.0:
                VOLTAGE_FACTOR = 0.5
            elif direction > 0.0:
                left_speed = (
                    left_speed / speed_multiplier
                )  # turn right (faster left wheel)
            else:
                right_speed = (
                    right_speed / speed_multiplier
                )  # turn left (faster right wheel)
        else:
            VOLTAGE_FACTOR = 0.25

            if direction >= 0.0:
                right_speed = (
                    right_speed * speed_multiplier
                )  # turn right (slower right wheel)
            else:
                left_speed = (
                    left_speed * speed_multiplier
                )  # turn left (slower left wheel)

        left_speed = left_speed * VOLTAGE_FACTOR
        right_speed = right_speed * VOLTAGE_FACTOR

        print(left_speed, right_speed)

        hummingbird_driver.move(left_speed, right_speed)

        await Tasks.yield_task(XboxJoystick.EVENT_LOOP_DELAY)
