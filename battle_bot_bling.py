from robot.tasks import Tasks


async def bling(bird):
    while True:
        print("bling active")

        await Tasks.yield_task(4.5)
