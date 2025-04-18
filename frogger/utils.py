import os
import json
import pygame

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')

# load JSON file
def load_data_file(filename):
    filepath = os.path.join(BASE_DIR, filename)
    with open(filepath, 'r') as file:
        return json.load(file)

# load image files, scale them, add to images dict, and return dict
def load_images(image_data):
    images = {}

    for obj_type in image_data:
        image = pygame.image.load(image_data[obj_type]['image'])
        image_scaled = pygame.transform.scale(image, (image_data[obj_type]['width'], image_data[obj_type]['height']))
        images.update({obj_type: image_scaled})
    
    return images

# return image based on image_type (string)
def get_image(images, image_type):
    return images[image_type]

# create all game objects, store in objects array, and return the array
def load_objects(level_map, images, object_factory):
    objects = []

    for level_data in level_map['levels']:
        for row, lane_data in enumerate(level_data['lanes']):
            for col, object_data in enumerate(lane_data['objects']):
                if object_data:
                    x = col * lane_data['width']
                    y = (row + 1) * lane_data['height']
                    objects.append(object_factory(object_data, images, x, y, lane_data['movement']))

    return objects