from robot.tasks import Tasks
from robot.xbox_controller import XboxController
from time import sleep


def driving(hummingbird, event_queue):
    running = True

    while running:
        controller_state = event_queue.get()

        # speed = -controller_state.left_y() * 100

        # if speed != 0.0:
        #   print("Speed", speed)

        # sleep(XboxController.EVENT_LOOP_DELAY)
        # --------------------------------------------------------------------------------------------------------------
        #  exit
        # --------------------------------------------------------------------------------------------------------------
        if controller_state.button_down_milliseconds(XboxController.BUTTON_XBOX):
            running = False
            break

        # --------------------------------------------------------------------------------------------------------------
        #  driving
        # --------------------------------------------------------------------------------------------------------------
        FACTOR = 0.75

        left_speed = right_speed = round(-controller_state.left_y() * 100, 2) + 0.0

        speed_multiplier = 1.0 - (abs(controller_state.right_x()) * FACTOR)

        if controller_state.right_x() >= 0.0:
            right_speed = (
                right_speed * speed_multiplier
            )  # turn right (slower right wheel)
        else:
            left_speed = left_speed * speed_multiplier  # turn left (slower left wheel)

        hummingbird.move(left_speed, right_speed)

        # --------------------------------------------------------------------------------------------------------------
        #  weapons
        # --------------------------------------------------------------------------------------------------------------
        left_weapon = controller_state.left_trigger() * 100.0
        right_weapon = controller_state.right_trigger() * 100.0

        # sleep(XboxController.EVENT_LOOP_DELAY)

        # return True
