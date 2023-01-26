import pygame
import sys
import settings
import ship
from bullet import Bullet
from alien import Alien
class Game:
    def __init__(self):
        self.settings = settings.Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption('Game')
        self.ship = ship.Ship(self)
        self.bullet = pygame.sprite.Group()
        self.alien = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        while True:
            self.check_event()
            self.update_screen() 
            self.ship.move_ship()
            self.bullet.update()
            
    def check_event(self):
        
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:    
                    self.check_keydown_event(event)
                elif event.type == pygame.KEYUP:
                    self.check_keyup_event(event)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   

    def check_keyup_event(self,event):
        if event.key == pygame.K_a:
            self.ship.moving_left = False
        if event.key == pygame.K_d:
            self.ship.moving_right = False
        if event.key == pygame.K_q:
            sys.exit()

    def check_keydown_event(self,event):
        if event.key == pygame.K_a:
            self.ship.moving_left = True
        if event.key == pygame.K_d:
            self.ship.moving_right = True
        if event.key == pygame.K_j:
            self.update_bullet()

    def update_bullet(self):
        new_bullet = Bullet(self)
        self.bullet.add(new_bullet)
        for bullet in self.bullet:
            if bullet.rect.bottom <= 0:
                self.bullet.remove(bullet)
                print(len(self.bullet))

    def _create_fleet(self):
        alien = Alien(self)
        alien.width,alien.height = alien.rect.size
        ship_height = self.ship.rect.height
        avaliable_space_x = self.settings.screen_width - alien.width
        avaliable_space_row = self.settings.screen_height - 2*alien.height - ship_height
        alien_number_x = avaliable_space_x //   alien.width
        alien_number_row = avaliable_space_row //  alien.height
        for number_row in range(alien_number_row):
            for number_alien in range(alien_number_x):
                self._create_alien(number_row,number_alien)

    def _create_alien(self,number_row,number_alien): 
        alien = Alien(self)
        self.alien.add(alien)
        alien.width,alien.height = alien.rect.size
        alien.x = alien.width + alien.width * number_alien
        alien.rect.x = alien.x

        
    
    def update_screen(self):
        self.screen.fill(self.settings.screen_color)
        self.ship.blitme()
        for bullet in self.bullet.sprites():
            bullet.draw_bullet()
        self.alien.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    game = Game()
    game.run_game()



