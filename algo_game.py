import pygame

from random import choice

from data.settings import clock
from data.interface import MainMenu, MenuPointer, Etc
from data.levels.runner import RunnerLevel
from data.levels.lobby import Lobby


pygame.init()

menu = MainMenu()
pointer = MenuPointer()
runner = RunnerLevel()

current_stage = 0
running = True
start_time = 0

# Timer
runner_timer = pygame.USEREVENT + 1
pygame.time.set_timer(runner_timer, 1000)

while running:
    for event in pygame.event.get():
        # pygame.QUIT event means the user clicked X to close your window
        if event.type == pygame.QUIT or current_stage == -1:
            running = False

        # Where to go from game over screen
        elif event.type == pygame.KEYDOWN and current_stage == -2:
            if event.key == pygame.K_ESCAPE:
                current_stage = 0
            else:
                current_stage = 1

        # Every second generate enemy on runner
        if event.type == runner_timer and current_stage == 1:
            runner.tick(choice(['flying', 'sneaky', 'sneaky']))

    # Main Menu
    if current_stage == 0:
        clock.tick(15)
        current_stage = menu.use_main_menu(pointer)
        if current_stage == 1:
            start_time = int(pygame.time.get_ticks() / 1000)

    # Runner mini game
    elif current_stage == 1:
        current_stage = runner.show(start_time)

    # Lobby
    elif current_stage == 2:
        Lobby().show()

    # Game over
    elif current_stage == -2:
        start_time = Etc().game_over()

    clock.tick(60)

    # Put work on screen
    pygame.display.flip()

pygame.quit()
