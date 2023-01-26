import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self,game) -> None:
        super().__init__()
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)

        self.rect.midtop = game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.settings.bullet_color,self.rect)
        