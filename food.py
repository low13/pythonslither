import pygame
import random

class Food:
    def __init__(self, screen, pos: tuple=None):
        if pos:
            self.rect = pygame.Rect(pos[0], pos[1], 40, 40)
        else:
            self.rect = pygame.Rect(random.randint(0, 14) * 40, random.randint(0, 9) * 40, 40, 40)
        pygame.draw.rect(screen, "red", self.rect)