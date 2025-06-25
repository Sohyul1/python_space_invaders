import pygame, sys
from spaceship import Spaceship

pygame.init()

screen_width = 800
screen_height = 700

grey = (29,29,27)

screen  = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pyhton Space Invaders")

clock =  pygame.time.Clock()

spaceship = Spaceship(screen_width, screen_height)
spaceship_group =  pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)

while True:
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # updating
        spaceship_group.update()

        # Drawing 
        screen.fill(grey)
        spaceship_group.draw(screen)
        spaceship_group.sprite.laser_group.draw(screen)
        pygame.display.update()
        clock.tick(60)

