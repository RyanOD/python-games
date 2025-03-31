import pygame
from config import SHIP_IMAGE

class Ship:
    def __init__(self):
        self.alive = True
        self.image = SHIP_IMAGE