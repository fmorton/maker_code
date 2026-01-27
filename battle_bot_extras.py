from robot.tasks import Tasks
from robot.xbox_joystick import XboxJoystick


async def extras(hummingbird, joystick):
    running = True

    while running:
        if joystick.state.button_down_milliseconds(XboxJoystick.BUTTON_A):
            print(
                "Extra button A",
                joystick.state.button_down_milliseconds(XboxJoystick.BUTTON_A),
            )

        await Tasks.yield_task(XboxJoystick.EVENT_LOOP_DELAY)
