from robot.tasks import Tasks
from robot.xbox_joystick import XboxJoystick


async def weapons(hummingbird, joystick):
    running = True

    while running:
        if joystick.state.left_trigger():
            print("Shoot left trigger", joystick.state.left_trigger())

        if joystick.state.right_trigger():
            print("Shoot right trigger", joystick.state.right_trigger())

        await Tasks.yield_task(XboxJoystick.EVENT_LOOP_DELAY)
