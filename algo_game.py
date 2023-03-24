import pygame
from game_interface import Menus
from settings import screen, clock

# pygame setup

pygame.init()
menu = Menus()
running = True
dt = 0


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    menu.show_main()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        ...
    if keys[pygame.K_s]:
        ...

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()