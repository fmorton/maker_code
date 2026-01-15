from robot.tasks import Tasks
import pygame


def weapons_button_pressed(hummingbird, instance_id, button):
    print("Weapons Button Pressed:", button)


async def weapons(hummingbird, joystick):
    while True:
        print("Weapons Active")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.JOYBUTTONDOWN:
                weapons_button_pressed(hummingbird, event.instance_id, event.button)

        await Tasks.yield_task(3.5)
