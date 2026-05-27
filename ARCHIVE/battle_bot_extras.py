from robot.tasks import Tasks
from robot.xbox_controller import XboxController


async def extras(hummingbird, controller):
    running = True

    while running:
        if controller.state.button_down_milliseconds(XboxController.BUTTON_A):
            print(
                "Extra button A",
                controller.state.button_down_milliseconds(XboxController.BUTTON_A),
            )

        await Tasks.yield_task(XboxController.EVENT_LOOP_DELAY)
