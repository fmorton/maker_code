from robot.tasks import Tasks
import random


class State:
    def __init__(self):
        self.random_number = 0


async def task_1(state):
    while True:
        state.random_number = random.randint(0, 100)

        print("task_1 running", state.random_number)

        await Tasks.yield_task(1.0)


async def task_2(state):
    while True:
        print("task_2 running", state.random_number)

        await Tasks.yield_task(0.5)


tasks = Tasks()
state = State()

tasks.create_task(task_1(state))
tasks.create_task(task_2(state))

tasks.run()
