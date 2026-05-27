from robot.hummingbird_l298n_dual_motor_driver import HummingbirdL298nDualMotorDriver
from robot.hummingbird_tb6612fng_dual_motor_driver import (
    HummingbirdTb6612fngDualMotorDriver,
)
from robot.tasks import Tasks
from robot.xbox_controller import XboxController
from time import sleep


async def driving(hummingbird, controller):
    running = True

    hummingbird_driver = HummingbirdL298nDualMotorDriver(hummingbird)
    # hummingbird_driver = HummingbirdTb6612fngDualMotorDriver(hummingbird)

    while running:
        # --------------------------------------------------------------------------------------------------------------
        #  driving
        # --------------------------------------------------------------------------------------------------------------
        FACTOR = 0.75
        VOLTAGE_FACTOR = 0.25

        if controller.state.button_down_seconds(3) > 0.0:
            VOLTAGE_FACTOR = 0.60

        left_speed = right_speed = round(-controller.state.left_y() * 100, 2) + 0.0

        speed_multiplier = 1.0 - (abs(controller.state.right_x()) * FACTOR)

        left_speed = left_speed * VOLTAGE_FACTOR
        right_speed = right_speed * VOLTAGE_FACTOR

        if controller.state.right_x() >= 0.0:
            right_speed = (
                right_speed * speed_multiplier
            )  # turn right (slower right wheel)
        else:
            left_speed = left_speed * speed_multiplier  # turn left (slower left wheel)

        hummingbird_driver.move(left_speed, right_speed)

        await Tasks.yield_task(XboxController.EVENT_LOOP_DELAY)
