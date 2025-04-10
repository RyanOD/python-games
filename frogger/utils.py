import os
import json
import pygame

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')

def load_data_file(filename):
    filepath = os.path.join(BASE_DIR, filename)
    with open(filepath, 'r') as file:
        return json.load(file)

def load_images(image_data):
    images = {}
    for obj_type in image_data:
        image = pygame.image.load(image_data[obj_type]['image'])
        image_scaled = pygame.transform.scale(image, (image_data[obj_type]['width'], image_data[obj_type]['height']))
        images.update({obj_type: image_scaled})
    return images

def get_image(images, image_type):
    return images[image_type]