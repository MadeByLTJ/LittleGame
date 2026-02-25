import pygame
from const import *
from block import *
from levels import *
import os

class Game:
    def __init__(self):
        pygame.mixer.init()
        self.base_path = os.path.dirname(__file__)
        self.kick_sound = pygame.mixer.Sound(os.path.join(self.base_path, "snd", "kick.wav"))
        self.hit_sound = pygame.mixer.Sound(os.path.join(self.base_path, "snd", "hihat.wav"))
        self.x = 32
        self.y = 32
        self.blocks = []
        self.score = 0
        self.load()
    
    def load(self):
        try:
            with open(os.path.join(self.base_path, "progress"), "r", encoding="utf-8") as f:
                self.level, self.m = f.readlines()
                self.level = int(self.level.split("\n")[0])
                self.m = int(self.m.split("\n")[0])
            if self.level > len(levels):
                raise Exception
        except:
            self.level = 1
            self.m = 0

    def update(self, screen):
        font = pygame.font.Font(None, 36)
        score_surface = font.render(f"LEVEL {self.level}        Score: {self.score}        Money: {self.m}", True, BLACK)
        screen.blit(score_surface, (10, 10))
        if not self.blocks:
            return
        for block in self.blocks:
            hits = block.move()
            if hits > 0:
                self.kick_sound.play()
            self.score += hits
        for block in self.blocks:
            screen.blit(block.block_image, block.block_image_rect)
        if self.score > levels[self.level][1]:
            self.m += levels[self.level][2]
            self.level += 1
            self.score = 0
            self.blocks.clear()

    def add_a_block(self, event):
        if self.level > len(levels):
            return
        if event.type == pygame.MOUSEBUTTONDOWN:
            if len(self.blocks) < levels[self.level][0]:
                self.x, self.y = pygame.mouse.get_pos()
                self.blocks.append(Block(self.x, self.y))
                self.kick_sound.stop()
                self.hit_sound.play()
    
    def save(self):
        with open(os.path.join(self.base_path, "progress"), "w", encoding="utf-8") as f:
            f.write(str(self.level)+"\n"+str(self.m)+"\n")
