import pygame

from robot.tasks import Tasks
from robot.xbox_joystick import XboxJoystick


async def event_manager(joystick, debugging=False):
    running = True

    while running:
        for event in pygame.event.get():
            joystick.state.event(event, debugging)

            if event.type == pygame.QUIT:
                running = False

        await Tasks.yield_task(XboxJoystick.EVENT_LOOP_DELAY)
