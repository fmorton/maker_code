from robot.tasks import Tasks
import pygame
import sys
import time
import os

def get_joystick():
    os.environ["SDL_VIDEODRIVER"] = "dummy"

    pygame.init()
    pygame.joystick.init()

    # Get the number of connected joysticks
    joystick_count = pygame.joystick.get_count()
    print(f"Number of joysticks: {joystick_count}")

    if joystick_count == 0:
        print("No Joystick Available")
        exit(200)

    # Initialize and store joystick objects
    joysticks = []
    #for i in range(joystick_count):
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    joysticks.append(joystick)
    print(f"Initialized joystick: {joystick.get_name()}")

    return joystick

async def driving(hummingbird):

    #pygame.init()
    #pygame.joystick.init()

    #while pygame.joystick.get_count() == 0:
    #    print("Waiting for an xbox joystick")
    #    time.sleep(0.5)

    #joystick = pygame.joystick.Joystick(0)
    joystick = get_joystick()

    while True:
        print("driving active")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.JOYBUTTONDOWN:
                print(f"Joystick {event.instance_id} button {event.button} pressed")
            elif event.type == pygame.JOYAXISMOTION:
                print(
                    f"Joystick {event.instance_id} axis {event.axis} motion: {event.value}"
                )
            elif event.type == pygame.JOYHATMOTION:
                print(f"Joystick {event.instance_id} hat {event.hat} motion: {event.value}")

        #hummingbird.move(50, 50)
        #time.sleep(0.5)
        ## hummingbird.move_right_motor(0)
        #hummingbird.move(0, 0)

        await Tasks.yield_task(0.005)
