import asyncio
import pygame

from robot.tasks import Tasks


def weapons_button_pressed(hummingbird, instance_id, button):
    if button in [9, 10]:  # right/left trigger
        print("Shoot")


async def weapons(hummingbird, joystick, weapons_queue):
    running = True

    while running:
        try:
            event = weapons_queue.get_nowait()

            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.JOYBUTTONDOWN:
                weapons_button_pressed(hummingbird, event.instance_id, event.button)
        except asyncio.QueueEmpty:
            pass

        await Tasks.yield_task(0.0)
