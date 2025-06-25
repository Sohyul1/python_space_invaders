import pygame, sys
from game import Game

pygame.init()

screen_width = 800
screen_height = 700

grey = (29,29,27)

screen  = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pyhton Space Invaders")

clock =  pygame.time.Clock()

game = Game(screen_width, screen_height,)

while True: 
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Updating
        game.spaceship_group.update()
        # Drawing 
        screen.fill(grey)
        game.spaceship_group.draw()
        game.spaceship_group.sprite.laser_group.draw(screen)
        pygame.display.update()
        clock.tick(60)

