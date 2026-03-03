from robot.tasks import Tasks
from robot.xbox_joystick import XboxJoystick


async def driving(hummingbird, joystick):
    running = True

    while running:
        speed = -joystick.state.left_y() * 100

        if speed != 0.0:
            print("Speed", speed)

        await Tasks.yield_task(XboxJoystick.EVENT_LOOP_DELAY)
