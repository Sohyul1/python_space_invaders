import pygame
from spaceship import Spaceship

class Game:
	def __init__(self, screen_width, screen_height, offset):
		self.screen_width = screen_width
		self.screen_height = screen_height
		self.offset = offset
		self.spaceship_group = pygame.sprite.GroupSingle()
		self.spaceship_group.add(Spaceship(self.screen_width, self.screen_height, self.offset))