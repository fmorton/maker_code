from robot.tasks import Tasks


async def driving(bird):
    while True:
        print("driving active")

        await Tasks.yield_task(1.0)
