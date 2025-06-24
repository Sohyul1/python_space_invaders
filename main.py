import pygame, sys

pygame.init

screen_width = 800
screen_height = 700

grey = (29,29,27)

screen  = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pyhton Space Invaders")

clock =  pygame.time.Clock()

while True:
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # Drawing 
        screen.fill(grey)
        
        pygame.display.update()
        clock.tick(60)