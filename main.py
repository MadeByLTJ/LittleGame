import pygame
from const import *
from game import *

pygame.init()
pygame.display.set_caption("小game")
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

game = Game()

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        game.add_a_block(event)
    
    screen.fill(WHITE)
    game.update(screen)
    pygame.display.flip()

game.save()
pygame.quit()
