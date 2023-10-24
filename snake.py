import pygame
from enum import Enum

class Snake:
    def __init__(self):
        self.direction = Direction.NONE
        self.squares = [[280, 200]]

class Direction(Enum):
    NONE = 0
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4