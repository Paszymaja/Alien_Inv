import pygame
import random
from pygame.sprite import Sprite


class Enemy(Sprite):
    def __init__(self, screen, settings):
        super(Enemy, self).__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load('Sprites/Enemy.png')
        self.rect = self.image.get_rect()

        self.rect.x = random.randint(30, 1200)
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.rect.y += 1