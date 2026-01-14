import os
import pygame

os.environ["SDL_VIDEODRIVER"] = "dummy"
pygame.init()

running = True
while running:
    # Event handling
    for event in pygame.event.get():
        print("event is", event)
        if event.type == pygame.QUIT:
            running = False

        # Check for KEYDOWN event
        if event.type == pygame.KEYDOWN:
            # Detect specific key press
            if event.key == pygame.K_SPACE:
                print("Spacebar pressed!")
            elif event.key == pygame.K_RETURN:
                print("Enter key pressed!")
            elif event.key == pygame.K_ESCAPE:
                print("Escape key pressed! Exiting...")
                running = False

    # Game logic and drawing (not directly related to input, but part of loop)
    # screen.fill((0, 0, 0)) # Fill screen with black
    # pygame.display.flip() # Update the display
print("DONE")
