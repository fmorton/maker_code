from robot.tasks import Tasks
import pygame
import sys
from time import sleep


def driving_button_pressed(hummingbird, instance_id, button):
    print("Driving Button Pressed:", button)


def driving_joystick_moved(hummingbird, instance_id, axis, value, joystick_minimum):
    if abs(value) < joystick_minimum:
        return

    print("Joystick Axis:", axis, " Value:", value)

    # hummingbird.move(50, 50)
    # sleep(0.1)
    # hummingbird.move(0, 0)


async def driving(hummingbird, joystick, joystick_minimum=0.25):
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # elif event.type == pygame.JOYBUTTONDOWN:
            #    driving_button_pressed(hummingbird, event.instance_id, event.button)
            elif event.type == pygame.JOYAXISMOTION:
                driving_joystick_moved(
                    hummingbird,
                    event.instance_id,
                    event.axis,
                    event.value,
                    joystick_minimum,
                )

        await Tasks.yield_task(0.0)
