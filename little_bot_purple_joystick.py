import os
import pygame
import sys
import time

os.environ["SDL_VIDEODRIVER"] = "dummy"

SIDE_TO_SIDE_SERVO = 2
SIDE_TO_SIDE_CENTER = 75
UP_DOWN_CENTER = 75
UP_DOWN_SERVO = 1

from robot.hummingbird import Hummingbird

hummingbird = Hummingbird("A")

pygame.init()
pygame.joystick.init()

while pygame.joystick.get_count() == 0:
    print("Waiting for an xbox joystick")
    time.sleep(0.5)

joystick = pygame.joystick.Joystick(0)

# screen = pygame.display.set_mode((600, 400))
# pygame.display.set_caption("Pygame Joystick Test")

running = True

hummingbird.position_servo(SIDE_TO_SIDE_SERVO, SIDE_TO_SIDE_CENTER)
hummingbird.position_servo(UP_DOWN_SERVO, UP_DOWN_CENTER)

while running:
    for event in pygame.event.get():
        if event.type == pygame.JOYAXISMOTION:
            if event.axis == 0:
                side_to_side = SIDE_TO_SIDE_CENTER + event.value * 35
                # print("axis 1:", event.value, "side_to_side", side_to_side)
                hummingbird.position_servo(SIDE_TO_SIDE_SERVO, side_to_side)
            elif event.axis == 1:
                up_down = UP_DOWN_CENTER + event.value * 15
                # print("Y:", event.value,up_down)
                hummingbird.position_servo(UP_DOWN_SERVO, up_down)

    # screen.fill((255, 255, 0))
    # pygame.display.flip()
    # time.sleep(0.1)

pygame.quit()
sys.exit()
