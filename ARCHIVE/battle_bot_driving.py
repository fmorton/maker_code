from robot.tasks import Tasks
from robot.xbox_controller import XboxController
from time import sleep


async def driving(hummingbird, controller):
    running = True

    while running:
        # --------------------------------------------------------------------------------------------------------------
        #  driving
        # --------------------------------------------------------------------------------------------------------------
        FACTOR = 0.75

        left_speed = right_speed = round(-controller.state.left_y() * 100, 2) + 0.0

        speed_multiplier = 1.0 - (abs(controller.state.right_x()) * FACTOR)

        if controller.state.right_x() >= 0.0:
            right_speed = (
                right_speed * speed_multiplier
            )  # turn right (slower right wheel)
        else:
            left_speed = left_speed * speed_multiplier  # turn left (slower left wheel)

        hummingbird.move(left_speed, right_speed)

        await Tasks.yield_task(XboxController.EVENT_LOOP_DELAY)
