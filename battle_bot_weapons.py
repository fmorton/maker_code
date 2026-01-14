from robot.tasks import Tasks


async def weapons(bird):
    while True:
        print("weapons active")

        await Tasks.yield_task(4.5)
