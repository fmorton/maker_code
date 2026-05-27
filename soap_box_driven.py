import pygame

from robot.hummingbird import Hummingbird
from robot.xbox_controller import XboxController
from time import sleep

hummingbird = Hummingbird("A")
controller = XboxController().connect()

print("Soap Box Car Ready To Drive")

STRAIGHT = 90.0
MAX_DEGREES = 23.0

while True:
    for event in pygame.event.get():
        controller.state.event(event, False)

    direction = controller.state.right_x()
    angle = 0.0

    print(direction, angle)

    hummingbird.position_servo(1, 115)
    sleep(0.1)
