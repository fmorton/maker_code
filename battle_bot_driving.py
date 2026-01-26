import asyncio
import math
import pygame

from robot.tasks import Tasks
from time import sleep


def driving_button_pressed(hummingbird, instance_id, button):
    pass


def driving_joystick_moved(
    hummingbird, joystick, instance_id, axis, value, joystick_minimum
):
    if abs(value) < joystick_minimum:
        return

    speed = -value * 100

    print("Joystick Axis Driving:", axis, " Value:", value, "Speed:", speed)

    if axis == 1:
        if abs(speed) < 50:
            speed = 0

        print(
            "DEBUG: DRIVING================================================================================================",
            speed,
        )
        hummingbird.move(speed, speed)
        # sleep(0.25)
        # hummingbird.move(0, 0)


async def driving(driving_queue, hummingbird, joystick, joystick_minimum=0.40):
    running = True

    while running:
        left_x_axis = joystick.joystick.get_axis(0)
        left_y_axis = joystick.joystick.get_axis(1)

        if abs(left_x_axis) < joystick_minimum:
            left_x_axis = 0.0
        if abs(left_y_axis) < joystick_minimum:
            left_y_axis = 0.0

        speed = math.sqrt(left_x_axis**2 + left_y_axis**2)

        if left_y_axis != 0.0:
            print("left_y_axis: ", left_y_axis)

        if speed > 1.0:
            speed = 1.0

        angle_rad = math.atan2(-left_y_axis, left_x_axis)
        angle_deg = math.degrees(angle_rad)
        # if angle_deg < 0:
        #    angle_deg += 360
        # print(
        #    "Axis:", left_x_axis, left_y_axis, "  speed:", speed, "  angle", angle_deg
        # )

        try:
            event = driving_queue.get_nowait()

            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.JOYBUTTONDOWN:
                driving_button_pressed(hummingbird, event.instance_id, event.button)
            elif event.type == pygame.JOYAXISMOTION:
                driving_joystick_moved(
                    hummingbird,
                    event.instance_id,
                    event.axis,
                    event.value,
                    joystick_minimum,
                )
        except asyncio.QueueEmpty:
            pass

        await Tasks.yield_task(0.0)
