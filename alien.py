import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,game) -> None:
        super().__init__()

        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load('python\\image\\1.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
