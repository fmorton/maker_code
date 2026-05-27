import pygame
import sys
import time

pygame.init()
pygame.controller.init()

# Get the number of connected controllers
controller_count = pygame.controller.get_count()
print(f"Number of controllers: {controller_count}")

if controller_count == 0:
    print("No Joystick Available")
    exit(200)

# Initialize and store controller objects
controllers = []
for i in range(controller_count):
    controller = pygame.controller.Joystick(i)
    controller.init()
    controllers.append(controller)
    print(f"Initialized controller {i}: {controller.get_name()}")

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Pygame Joystick Test")

running = True
while running:
    print("Running....")
    # pygame.event.pump()
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

    screen.fill((255, 255, 0))
    pygame.display.flip()
    time.sleep(0.5)

pygame.quit()
sys.exit()
