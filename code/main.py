import pygame
import sprites.player as pl
import sprites.star as star
from os.path import join
from random import randint

#general setup
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 1180, 620
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Shooter")
running = True
clock = pygame.time.Clock()

star_surf = pygame.image.load(join("images", "star.png")).convert_alpha()
all_sprites = pygame.sprite.Group()
for i in range(20):
    star.Star(all_sprites, star_surf, SCREEN_WIDTH, SCREEN_HEIGHT)
player = pl.Player(all_sprites, SCREEN_WIDTH, SCREEN_HEIGHT)    

meteor_surf = pygame.image.load(join("images", "meteor.png")).convert_alpha()
meteor_rect = meteor_surf.get_frect(center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2))

laser_surf = pygame.image.load(join("images", "laser.png")).convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft = (20, SCREEN_HEIGHT - 20))

#custom events
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 500)

while running:
    dt = clock.tick() / 1000
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == meteor_event:
            print("create meteor")    

    #update  
    all_sprites.update(dt)
    
    #draw the game
    display_surface.fill("darkgrey")
         
    all_sprites.draw(display_surface)

    pygame.display.update()            

pygame.quit()            

