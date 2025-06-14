import pygame
from os.path import join
from random import randint

#general setup
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 1180, 620
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Shooter")
running = True
clock = pygame.time.Clock()

#plain surface
surf = pygame.Surface((100, 200))
surf.fill("orange")
x = 100
y = 150

#imports
player_surf = pygame.image.load(join("images", "player.png")).convert_alpha()
player_rect = player_surf.get_frect(center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
player_direction = 1
player_speed = 0.4

star_surf = pygame.image.load(join("images", "star.png")).convert_alpha()
star_positions = [(randint(0, SCREEN_WIDTH), randint(0, SCREEN_HEIGHT)) for _ in range(20)]

meteor_surf = pygame.image.load(join("images", "meteor.png")).convert_alpha()
meteor_rect = meteor_surf.get_frect(center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2))

laser_surf = pygame.image.load(join("images", "laser.png")).convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft = (20, SCREEN_HEIGHT - 20))

while running:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #draw the game
    display_surface.fill("darkgrey")
    for star_pos in star_positions:
        display_surface.blit(star_surf, star_pos)
        
    #player's movement 
    player_rect.x += player_direction * player_speed 
    if player_rect.right > SCREEN_WIDTH or player_rect.left < 0:
        player_direction *= -1
          
            
    #if player_rect.right < SCREEN_WIDTH:
    #    player_rect.left += 0.2

    display_surface.blit(meteor_surf, meteor_rect)   
    display_surface.blit(laser_surf, laser_rect)     
    display_surface.blit(player_surf, player_rect) 

    pygame.display.update()            

pygame.quit()            

