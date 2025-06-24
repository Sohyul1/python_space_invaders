import pygame
class Spaceship(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_heigth):
        super().__init__()
        self.screen_width = screen_width
        self.screen_heigth = screen_heigth
        self.image = pygame.image.load("Graphics/spaceship.png")
        self.rect = self.image.get_rect(midbottom = (self.screen_width/2, self.screen_heigth))      