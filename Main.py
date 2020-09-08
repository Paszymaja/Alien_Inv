import pygame
from pygame.sprite import Group

from src import game_functions as gf
from src.background import Background
from src.button import Button
from settings import Settings
from src.ship import Ship
from src.stats import GameStats


def run_game():
    pygame.init()
    screen_settings = Settings()
    stats = GameStats(screen_settings)

    screen = pygame.display.set_mode((screen_settings.screen_width, screen_settings.screen_height))
    ship = Ship(screen)
    pygame.display.set_caption('Alien Inv')
    screen_y = 0
    background = Background(screen_settings.bg_image, [0, 0])
    play_button = Button(screen_settings, screen, "Play")
    bullets = Group()
    enemies = Group()

    while True:  # Game Loop
        gf.check_events(screen_settings, screen, ship, bullets, stats, play_button, enemies, )
        if stats.game_active:
            ship.update()
            gf.update_bullets(bullets, enemies)
            gf.update_enemies(enemies, ship, screen_settings, stats, screen, bullets)
        gf.update_screen(screen_settings, screen, ship, screen_y, background, bullets, enemies, play_button, stats)
        screen_y += screen_settings.bg_speed


run_game()
