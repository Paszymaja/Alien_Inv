import pygame

from settings import Settings


class Ship:
    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load('Sprites/Ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def blitme(self):
        self.screen.blit(self.image, self.rect)


    def update(self):
        ship_settings = Settings()
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += ship_settings.ship_speed
            self.image = pygame.image.load('Sprites/ship_right.png')
        elif self.moving_left and self.rect.left > 0:
            self.rect.centerx -= ship_settings.ship_speed
            self.image = pygame.image.load('Sprites/ship_left.png')
        elif self.moving_up and self.rect.top > 0:
            self.rect.centery -= ship_settings.ship_speed
            self.image = pygame.image.load('Sprites/ship_up.png')
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += ship_settings.ship_speed
            self.image = pygame.image.load('Sprites/ship_down.png')
        else:
            self.image = pygame.image.load('Sprites/Ship.png')


    def center_ship(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom




