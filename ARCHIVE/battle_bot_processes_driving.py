from robot.tasks import Tasks
from robot.xbox_joystick import XboxJoystick
from time import sleep


def driving(hummingbird, event_queue):
    running = True

    while running:
        joystick_state = event_queue.get()

        #speed = -joystick_state.left_y() * 100

        #if speed != 0.0:
        #   print("Speed", speed)

        #sleep(XboxJoystick.EVENT_LOOP_DELAY)
        # ----------------------------------------------------------------------------------------------------------------------
        #  exit
        # ----------------------------------------------------------------------------------------------------------------------
        if joystick_state.button_down_milliseconds(XboxJoystick.BUTTON_XBOX):
            running = False
            break

        # ----------------------------------------------------------------------------------------------------------------------
        #  driving
        # ----------------------------------------------------------------------------------------------------------------------
        FACTOR = 0.75

        left_speed = right_speed = round(-joystick_state.left_y() * 100, 2) + 0.0

        speed_multiplier = 1.0 - (abs(joystick_state.right_x()) * FACTOR)

        if joystick_state.right_x() >= 0.0:
            right_speed = right_speed * speed_multiplier  # turn right (slower right wheel)
        else:
            left_speed = left_speed * speed_multiplier  # turn left (slower left wheel)

        hummingbird.move(left_speed, right_speed)

        # ----------------------------------------------------------------------------------------------------------------------
        #  weapons
        # ----------------------------------------------------------------------------------------------------------------------
        left_weapon = joystick_state.left_trigger() * 100.0
        right_weapon = joystick_state.right_trigger() * 100.0


        #sleep(XboxJoystick.EVENT_LOOP_DELAY)

        #return True
