import pygame

from robot.tasks import Tasks
from robot.xbox_joystick import XboxJoystick
from time import sleep

def event_manager(event_queue, debugging=False):
    joystick = XboxJoystick().connect()

    print("Battlebot Ready")

    running = True

    while running:
        for event in pygame.event.get():
            joystick.state.event(event, debugging)

            event_queue.put(joystick.state)

            if event.type == pygame.QUIT:
                running = False

        #sleep(XboxJoystick.EVENT_LOOP_DELAY)
        # ----------------------------------------------------------------------------------------------------------------------
        #  state string
        # ----------------------------------------------------------------------------------------------------------------------
        if debugging:
            extra_state_string = ""
            extra_state_string += f"{left_weapon:8.2f}"
            extra_state_string += f"{right_weapon:8.2f}"
            extra_state_string += f"{left_speed:8.2f}"
            extra_state_string += f"{right_speed:8.2f}"
            extra_state_string += f"{speed_multiplier:8.2f}"

            joystick_state.print_state_string(extra_state_string)
