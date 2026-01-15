from robot.tasks import Tasks


async def extras(hummingbird, joystick):
    while True:
        print("Extras Active")

        await Tasks.yield_task(4.5)
