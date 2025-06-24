import pygame
class Spaceship(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_heigth):
        super().__init__()
        self.screen_width = screen_width
        self.screen_heigth = screen_heigth
        self.image = pygame.image.load("Graphics/spaceship.png")
        self.rect = self.image.get_rect(midbottom = (self.screen_width/2, self.screen_heigth))      
        self.speed = 6
    
    def get_user_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
                    
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

    def update(self):
	    self.get_user_input()
		