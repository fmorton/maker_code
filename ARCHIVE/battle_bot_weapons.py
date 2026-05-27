from robot.tasks import Tasks
from robot.xbox_controller import XboxController


async def weapons(hummingbird, controller):
    running = True

    while running:
        if controller.state.left_trigger():
            print("Shoot left trigger", controller.state.left_trigger())

        if controller.state.right_trigger():
            print("Shoot right trigger", controller.state.right_trigger())

        await Tasks.yield_task(XboxController.EVENT_LOOP_DELAY)
