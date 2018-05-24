import sys

import pygame

from settings import Settings


def run_game():
    pygame.init()

    screen_settings = Settings()
    screen = pygame.display.set_mode((screen_settings.screen_width, screen_settings.screen_height))
    pygame.display.set_caption('Alien Inv')

    while True:  # Game Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(screen_settings.bg_color)
        pygame.display.flip()


run_game()
