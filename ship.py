import pygame

from settings import Settings

class Ship():
    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load('Ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        ship_settings = Settings()
        if self.moving_right:
            self.rect.centerx += ship_settings.ship_speed
        elif self.moving_left:
            self.rect.centerx -= ship_settings.ship_speed