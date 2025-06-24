import pygame
class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Graphics/spaceship.png")
        self.rect = self.image.get_rect(midebottom = (100, 100))      