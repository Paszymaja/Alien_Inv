import sys

import pygame

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(screen_settings, screen, ship):
    screen.fill(screen_settings.bg_color)
    ship.blitme()
    pygame.display.flip()