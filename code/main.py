import pygame
from os.path import join

#general setup
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Shooter")
running = True

#plain surface
surf = pygame.Surface((100, 200))
surf.fill("orange")
x = 100
y = 150

#importing an image
player_surf = pygame.image.load(join("images", "player.png"))

while running:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #draw the game
    display_surface.fill("darkgrey")
    x += 0.1
    display_surface.blit(player_surf, (x, y))
    pygame.display.update()            

pygame.quit()            

