from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)
        self.image = pygame.image.load(join("images", "player", "down", "0.png")).convert_alpha()
        self.rect = self.image.get_frect(center = pos)

        #movement
        self.direction = pygame.math.Vector2()
        self.speed = 300
        self.collision_sprites = collision_sprites

    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction
        

    def move(self, dt):
        self.rect.x += self.direction.x * self.speed * dt  
        self.collision("horizontal")
        self.rect.y += self.direction.y * self.speed * dt 
        self.collision("vertical")

    def collision(self, direction):
        for col_sprite in self.collision_sprites:
            if col_sprite.rect.colliderect(self.rect):
                if direction == "horizontal":
                    if self.direction.x > 0: self.rect.right = col_sprite.rect.left
                    if self.direction.x < 0: self.rect.left = col_sprite.rect.right
                else:
                    if self.direction.y > 0: self.rect.bottom = col_sprite.rect.top
                    if self.direction.y < 0: self.rect.top = col_sprite.rect.bottom    

    def update(self, dt):
        self.input()
        self.move(dt)
        
        