from robot.hummingbird_l298n_dual_motor_driver import HummingbirdL298nDualMotorDriver
from robot.hummingbird_tb6612fng_dual_motor_driver import HummingbirdTb6612fngDualMotorDriver
from robot.tasks import Tasks
from robot.xbox_joystick import XboxJoystick
from time import sleep

async def driving(hummingbird, joystick):
    running = True

    #hummingbird_driver = HummingbirdL298nDualMotorDriver(hummingbird)
    hummingbird_driver = HummingbirdTb6612fngDualMotorDriver(hummingbird)

    while running:
        # ----------------------------------------------------------------------------------------------------------------------
        #  driving
        # ----------------------------------------------------------------------------------------------------------------------
        VOLTAGE_FACTOR = 0.25

        left_speed = right_speed = round(-joystick.state.left_y() * 100, 2) + 0.0

        left_speed = left_speed * VOLTAGE_FACTOR
        right_speed = right_speed * VOLTAGE_FACTOR

        direction = joystick.state.right_x()

        if direction == 0.0:
            pass
        elif direction > 0.0:
            print("Turn Right")
        else:
            print("Turn Left")

        hummingbird_driver.move(left_speed, right_speed)

        await Tasks.yield_task(XboxJoystick.EVENT_LOOP_DELAY)
