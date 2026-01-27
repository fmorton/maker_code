import pygame

from time import sleep
from robot.tasks import Tasks


async def event_manager(joystick, driving_queue, weapons_queue, extras_queue, debugging = False):
    running = True

    while running:
        for event in pygame.event.get():
            joystick.state.event(event, debugging)

            await driving_queue.put(event)
            await extras_queue.put(event)
            await weapons_queue.put(event)

            if event.type == pygame.QUIT:
                running = False

        await Tasks.yield_task(0.0)
