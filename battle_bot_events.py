import pygame

from robot.tasks import Tasks
from robot.xbox_controller import XboxController
from time import sleep


async def events(controller, debugging=False):
    running = True

    while running:
        for event in pygame.event.get():
            controller.state.event(event, debugging)

            if event.type == pygame.QUIT:
                running = False

        # --------------------------------------------------------------------------------------------------------------
        #  state string
        # --------------------------------------------------------------------------------------------------------------
        if debugging:
            extra_state_string = ""
            # extra_state_string += f"{left_weapon:8.2f}"
            # extra_state_string += f"{right_weapon:8.2f}"
            # extra_state_string += f"{left_speed:8.2f}"
            # extra_state_string += f"{right_speed:8.2f}"
            # extra_state_string += f"{speed_multiplier:8.2f}"

            controller.state.print_state_string(extra_state_string)

        controller.tick(30)

        await Tasks.yield_task(XboxController.EVENT_LOOP_DELAY)
