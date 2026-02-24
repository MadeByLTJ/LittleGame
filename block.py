import pygame
from const import *
from random import choice

class Block:
    def __init__(self, x, y):
        self.block_image = pygame.transform.scale(pygame.image.load("pic/player.png"), (64, 64))
        self.block_image_rect = self.block_image.get_rect(center=(x, y))
        self.speedx = BLOCK_SPEED * choice([-1, 1])
        self.speedy = BLOCK_SPEED * choice([-1, 1])
    
    def move(self):
        hit_count = 0
        self.block_image_rect.x += self.speedx
        self.block_image_rect.y += self.speedy
        if self.block_image_rect.right > WINDOW_WIDTH:
            self.block_image_rect.right = WINDOW_WIDTH
            self.speedx = -self.speedx
            hit_count += 1
        if self.block_image_rect.left < 0:
            self.block_image_rect.left = 0
            self.speedx = -self.speedx
            hit_count += 1
        if self.block_image_rect.bottom > WINDOW_HEIGHT:
            self.block_image_rect.bottom = WINDOW_HEIGHT
            self.speedy = -self.speedy
            hit_count += 1
        if self.block_image_rect.top < 0:
            self.block_image_rect.top = 0
            self.speedy = -self.speedy
            hit_count += 1

        return hit_count
