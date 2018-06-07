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

    while True:  # Game Loop
        gf.check_events(screen_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(screen_settings, screen, ship, screen_y, background, bullets)
        screen_y += screen_settings.bg_speed

        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
            print(len(bullets))



run_game()
