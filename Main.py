import pygame

from settings import Settings
from ship import Ship
from background import Background
from pygame.sprite import Group

import game_functions as gf


def run_game():
    pygame.init()
    screen_settings = Settings()

    screen = pygame.display.set_mode((screen_settings.screen_width, screen_settings.screen_height))
    ship = Ship(screen)
    pygame.display.set_caption('Alien Inv')
    screen_y = 0
    background = Background(screen_settings.bg_image, [0, 0])
    bullets = Group()
    enemies = Group()


    while True:  # Game Loop
        gf.check_events(screen_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets, enemies)
        gf.update_enemies(enemies)
        gf.update_screen(screen_settings, screen, ship, screen_y, background, bullets, enemies)
        screen_y += screen_settings.bg_speed




run_game()
