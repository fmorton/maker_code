import asyncio
import pygame

from robot.tasks import Tasks


def extras_button_pressed(hummingbird, instance_id, button):
    if button == 0:
        print("'A' Button Pressed")


async def extras(extras_queue, hummingbird, joystick):
    running = True

    while running:
        try:
            event = extras_queue.get_nowait()

            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.JOYBUTTONDOWN:
                extras_button_pressed(hummingbird, event.instance_id, event.button)
        except asyncio.QueueEmpty:
            pass

        await Tasks.yield_task(0.0)
