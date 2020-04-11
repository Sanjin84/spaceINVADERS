from constants import *
import pygame,random

class Hero(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.Surface([70, 20])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 480
        self.change_x = 0
        self.change_y = 0

    def update(self,surface):
        """ Move the bullet. """
        self.center_x = self.rect.x+35
        self.center_y = self.rect.y + 10
        self.rect.x += self.change_x
        self.rect.y += self.change_y
