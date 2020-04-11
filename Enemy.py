from constants import *
import pygame, random

class Enemy(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,680)
        self.rect.y = 20 + random.randint(1,10)*5
        self.change_x = 1
        self.change_y = 0

    def update(self,surface):
        """ Move the bullet. """
        self.center_x = self.rect.x + 35
        self.center_y = self.rect.y + 10
        self.rect.x += self.change_x
        if self.rect.x > 700 or self.rect.x < 0:
            self.change_x = -self.change_x
            self.rect.y += 5
