from robot.tasks import Tasks
from robot.xbox_joystick import XboxJoystick
from time import sleep

async def driving(hummingbird, joystick):
    running = True

    while running:
        # ----------------------------------------------------------------------------------------------------------------------
        #  driving
        # ----------------------------------------------------------------------------------------------------------------------
        FACTOR = 0.75

        left_speed = right_speed = round(-joystick.state.left_y() * 100, 2) + 0.0

        speed_multiplier = 1.0 - (abs(joystick.state.right_x()) * FACTOR)

        if joystick.state.right_x() >= 0.0:
            right_speed = right_speed * speed_multiplier  # turn right (slower right wheel)
        else:
            left_speed = left_speed * speed_multiplier  # turn left (slower left wheel)

        hummingbird.move(left_speed, right_speed)

        await Tasks.yield_task(XboxJoystick.EVENT_LOOP_DELAY)
