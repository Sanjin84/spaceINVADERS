from constants import *
import pygame, random, time, Hero, Bullet, Enemy
pygame.init()

all_sprites_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("OOP Game")
clock = pygame.time.Clock()

hero = Hero.Hero()
for i in range(0,10):
    enemy = Enemy.Enemy()
    enemy_list.add(enemy)
    all_sprites_list.add(enemy)

all_sprites_list.add(hero)

gameOn = True
while gameOn == True:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                hero.change_x = -5
            if event.key == pygame.K_RIGHT:
                hero.change_x = 5
            if event.key == pygame.K_1:
                print(len(all_sprites_list))
            if event.key == pygame.K_SPACE:
                bullet = Bullet.Bullet(hero.center_x, hero.center_y)
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)
        else:
            hero.change_x = 0

    if len(bullet_list) >0:
        for b in bullet_list:
            for e in enemy_list:
                b.check_collision(e)

    all_sprites_list.update(screen)
    all_sprites_list.draw(screen)
    clock.tick(60)
    pygame.display.flip()
