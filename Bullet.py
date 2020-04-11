from constants import *
import pygame

class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self,x=0,y=0):
        # Call the parent class (Sprite) constructor YEA YEs
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self,surface):
        """ Move the bullet. """
        self.rect.y -= 3
        pygame.draw.rect(surface, BLUE, [self.rect.x,self.rect.y, 10, 10])
        if self.rect.y < 0:
            self.kill()

    def check_collision(self, enemy):
        col = pygame.sprite.collide_rect(self,enemy)
        if col == True:
            self.kill()
            enemy.kill()
    
