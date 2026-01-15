import pygame

from time import sleep
from robot.tasks import Tasks

QUEUED_EVENTS = [pygame.QUIT, pygame.JOYBUTTONDOWN, pygame.JOYAXISMOTION]


async def event_manager(driving_queue, weapons_queue, extras_queue):
    running = True
    debugging = True

    while running:
        for event in pygame.event.get():
            if event.type in QUEUED_EVENTS:
                await driving_queue.put(event)
                await extras_queue.put(event)
                await weapons_queue.put(event)
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.JOYBUTTONDOWN:
                if debugging:
                    print("Button Pressed:", event.button)

        await Tasks.yield_task(0.0)
