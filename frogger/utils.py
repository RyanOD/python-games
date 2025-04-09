import os
import json
import pygame

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')

def load_data_file(filename):
    filepath = os.path.join(BASE_DIR, filename)
    with open(filepath, 'r') as file:
        return json.load(file)

def load_image(image, width, height):
    return pygame.transform.scale(pygame.image.load(image, (width, height)))