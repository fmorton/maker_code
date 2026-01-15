from robot.tasks import Tasks
import pygame
import sys
import time
import os


class XboxJoystick:
    def __init__(self, wait_for_joystick_message="Waiting for Xbox Controller"):
        self.connected = False
        self.joystick = None
        self.joystick_name = None

        os.environ["SDL_VIDEODRIVER"] = "dummy"

        pygame.init()
        pygame.joystick.init()

        if wait_for_joystick_message:
            while pygame.joystick.get_count() == 0:
                print(wait_for_joystick_message)
                time.sleep(1.0)

        if pygame.joystick.get_count() > 0:
            self.joystick = pygame.joystick.Joystick(0)

            self.joystick.init()

            self.joystick_name = self.joystick.get_name()

            self.connected = True


def driving_button_pressed(instance_id, button):
    print("Button Pressed:", button)


def driving_joystick_moved(instance_id, axis, value):
    if abs(value) < 0.2:
        return

    print("Joystick Axis:", axis, " Value:", value)


async def driving(hummingbird):
    running = True

    joystick = XboxJoystick()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.JOYBUTTONDOWN:
                driving_button_pressed(event.instance_id, event.button)
            elif event.type == pygame.JOYAXISMOTION:
                driving_joystick_moved(event.instance_id, event.axis, event.value)

        # hummingbird.move(50, 50)
        # time.sleep(0.5)
        ## hummingbird.move_right_motor(0)
        # hummingbird.move(0, 0)

        await Tasks.yield_task(0.005)
