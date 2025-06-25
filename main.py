import pygame, sys, random
from game import Game

pygame.init()

screen_width = 800
screen_height = 700
off_set = 50

grey = (29,29,27)
yellow = (243, 216, 63)

screen  = pygame.display.set_mode((screen_width, screen_height + (2 * off_set)))
pygame.display.set_caption("Pyhton Space Invaders")

clock =  pygame.time.Clock()

game = Game(screen_width, screen_height,)

shoot_laser = pygame.USEREVENT + 1
pygame.time.set_timer(shoot_laser, 600)

mystery_ship = pygame.USEREVENT + 2
pygame.time.set_timer(mystery_ship, random.randint(4000, 8000))

while True: 
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == shoot_laser and game.run:      
            for i in range(3):
                game.alien_shoot_laser()
        
        if  event.type == mystery_ship and game.run:
            game.create_mysterys_ship()
            pygame.time.set_timer(mystery_ship, random.randint(4000, 8000))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and game.run == False:
            game.reset()
        # Updating
    if game.run:
        game.spaceship_group.update()
        game.move_aliens()
        game.alien_lasers_group.update()
        game.mystery_ship_group.update()
        game.check_for_collisions()

        # Drawing 
    screen.fill(grey)
    pygame.draw.rect(screen, yellow, (10, 10, 780,780), 2, 0, 60, 60, 60, 60)
    game.spaceship_group.draw(screen)
    game.spaceship_group.sprite.laser_group.draw(screen)
    for obstacle in game.obstacles:
        obstacle.blocks_group.draw(screen)
    game.aliens_group.draw(screen)
    game.alien_lasers_group.draw(screen)
    game.mystery_ship_group.draw(screen)
    pygame.display.update()
    clock.tick(60)

