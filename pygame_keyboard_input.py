import os
import pygame

# Set the SDL_VIDEODRIVER environment variable to "dummy"
# This tells Pygame not to initialize the video system.
os.environ["SDL_VIDEODRIVER"] = "dummy"


pygame.init()
screen = pygame.display.set_mode((800, 600))
running = True

while running:
    print("running")
    for event in pygame.event.get():
        print(event.type)
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Spacebar pressed!")
            elif event.key == pygame.K_UP:
                print("Up arrow pressed!")
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                print("Spacebar released!")

    # Your other game logic and drawing code goes here
    # pygame.display.flip()

pygame.quit()
