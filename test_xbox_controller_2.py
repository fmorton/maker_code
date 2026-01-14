import pygame
import sys
import time

pygame.init()
pygame.joystick.init()

# Get the number of connected joysticks
joystick_count = pygame.joystick.get_count()
print(f"Number of joysticks: {joystick_count}")

if joystick_count == 0:
    print("No Joystick Available")
    exit(200)

# Initialize and store joystick objects
joysticks = []
for i in range(joystick_count):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()
    joysticks.append(joystick)
    print(f"Initialized joystick {i}: {joystick.get_name()}")

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
