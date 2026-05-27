import pygame

from robot.tasks import Tasks
from robot.xbox_controller import XboxController


async def event_manager(controller, debugging=False):
    running = True

    while running:
        for event in pygame.event.get():
            controller.state.event(event, debugging)

            if event.type == pygame.QUIT:
                running = False

        await Tasks.yield_task(XboxController.EVENT_LOOP_DELAY)
