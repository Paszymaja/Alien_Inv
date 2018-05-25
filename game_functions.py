import sys

import pygame

from background import Background



def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False


def update_screen(screen_settings, screen, ship):
    background = Background(screen_settings.bg_image, [0,0])
    screen.fill(screen_settings.bg_color)
    screen.blit(background.image, background.rect)
    ship.blitme()
    pygame.display.flip()
