import pygame

class Ship():
    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load('Ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.center_x = self.screen_rect.center_x
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):

        self.screen.blit(self.image, self.rect)