import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init()
    screen_settings = Settings()

    screen = pygame.display.set_mode((screen_settings.screen_width, screen_settings.screen_height))
    ship = Ship(screen)
    pygame.display.set_caption('Alien Inv')

    while True:  # Game Loop
        gf.check_events(ship)
        ship.update()
        gf.update_screen(screen_settings, screen, ship)


run_game()
