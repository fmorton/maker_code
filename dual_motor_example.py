from collections.abc import Sequence
from robot.hummingbird import Hummingbird

class HummingbirdDualMotorDriver:
    MINIMUM_SPEED = 30

    def __init__(self, device = 'A', minimum_speed = None):
        self.device = device
        self.minimum_speed = minimum_speed

        if minimum_speed is None: self.minimum_speed = self.MINIMUM_SPEED

        self.left_polarity = 1
        self.right_polarity = 1

        self.robot = Hummingbird(device)

    def reverse_left_polarity(self):
        self.left_polarity = -self.left_polarity

    def reverse_right_polarity(self):
        self.right_polarity = -self.right_polarity

    def reverse_polarity(self):
        reverse_left_polarity()
        reverse_right_polarity()

    def adjust_speed_for_polarity(self, speed, multiplier):
        return(speed * multiplier)

    def move_left_motor(self, speed):
        speed = self.adjust_speed_for_polarity(speed, self.left_polarity)

        if speed == 0 or (abs(speed) < self.minimum_speed):
            self.robot.tri_led(1, 0, 0, 0)
        elif speed > 0:
            self.robot.tri_led(1, abs(speed), 100, 0)
        else:
            self.robot.tri_led(1, abs(speed), 0, 100)

    def move_right_motor(self, speed):
        speed = self.adjust_speed_for_polarity(speed, self.right_polarity)

        if speed == 0 or (abs(speed) < self.minimum_speed):
            self.robot.tri_led(2, 0, 0, 0)
        elif speed > 0:
            self.robot.tri_led(2, 0, 100, abs(speed))
        else:
            self.robot.tri_led(2, 100, 0, abs(speed))

    def move(self, left_speed, right_speed = None):
        if isinstance(left_speed, Sequence):
            left_speed, right_speed = left_speed

        self.move_left_motor(left_speed)
        self.move_right_motor(right_speed)

    def stop(self):
        self.robot.tri_led(1, 0, 0, 0)
        self.robot.tri_led(2, 0, 0, 0)

    def stop_all(self):
        self.stop()
        self.robot.stop_all()


import os
import pygame
import sys
import time
#import HummingbirdDualMotorDriver

os.environ["SDL_VIDEODRIVER"] = "dummy"

SIDE_TO_SIDE_SERVO = 2
SIDE_TO_SIDE_CENTER = 75
UP_DOWN_CENTER = 75
UP_DOWN_SERVO = 1

from robot.hummingbird import Hummingbird

#hummingbird = Hummingbird("A")

hummingbird = HummingbirdDualMotorDriver('A')

pygame.init()
pygame.joystick.init()

while pygame.joystick.get_count() == 0:
    print("Waiting for an xbox joystick")
    time.sleep(0.5)
    
joystick = pygame.joystick.Joystick(0)

#screen = pygame.display.set_mode((600, 400))
#pygame.display.set_caption("Pygame Joystick Test")

running = True

#hummingbird.position_servo(SIDE_TO_SIDE_SERVO, SIDE_TO_SIDE_CENTER)
#hummingbird.position_servo(UP_DOWN_SERVO, UP_DOWN_CENTER)

while running:
    for event in pygame.event.get():
        #print("event.type:", event.type)
        if event.type == pygame.JOYAXISMOTION:
            print("event axis:",event.axis, "value:", event.value)
#            if event.axis == 0:
#                side_to_side = SIDE_TO_SIDE_CENTER + event.value * 35
#                #print("axis 1:", event.value, "side_to_side", side_to_side)
#                hummingbird.position_servo(SIDE_TO_SIDE_SERVO, side_to_side)
#            elif event.axis == 1:
#                up_down = UP_DOWN_CENTER + event.value * 15
#                #print("Y:", event.value,up_down)
#                hummingbird.position_servo(UP_DOWN_SERVO, up_down)

        print("DEBUG: move")
        #hummingbird.move_right_motor(50)
        hummingbird.move(50, 50)
        time.sleep(0.5)
        #hummingbird.move_right_motor(0)
        hummingbird.move(0, 0)
        time.sleep(0.5)
    #screen.fill((255, 255, 0))
    #pygame.display.flip()
    #time.sleep(0.1)

pygame.quit()
sys.exit()


