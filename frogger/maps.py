import pygame
import os
from utils import ASSETS_DIR

ROAD_EDGE = 960

BLUE = (0, 51, 153)
BLACK = (0, 0, 0)

OBJECT_MAP = {
    'F1': {'type': 'frog', 'height': 50, 'width': 50, 'image': 'frog_1.png'},
    'F2': {'type': 'frog', 'height': 50, 'width': 50, 'image': 'frog_2.png'},
    'F3': {'type': 'frog', 'height': 50, 'width': 50, 'image': 'frog_3.png'},
    'FH': {'type': 'frog', 'height': 50, 'width': 50, 'image': 'frog_home_1.png'},
    'FD1': {'type': 'frog', 'height': 60, 'width': 60, 'image': 'frog_dead_1.png'},
    'FD2': {'type': 'frog', 'height': 60, 'width': 60, 'image': 'frog_dead_2.png'},
    'FD3': {'type': 'frog', 'height': 60, 'width': 60, 'image': 'frog_dead_3.png'},
    'FD4': {'type': 'frog', 'height': 60, 'width': 60, 'image': 'frog_dead_4.png'},
    'T': {'type': 'turtle', 'height': 60, 'width': 60, 'image': 'turtle_1.png'},
    'LL': {'type': 'log', 'height': 60, 'width': 60, 'image': 'log_lt.png'},
    'LM': {'type': 'log', 'height': 60, 'width': 60, 'image': 'log_md.png'},
    'LR': {'type': 'log', 'height': 60, 'width': 60, 'image': 'log_rt.png'},
    'TL': {'type': 'truck', 'height': 60, 'width': 60, 'image': 'truck_lt.png'},
    'TR': {'type': 'truck', 'height': 60, 'width': 60, 'image': 'truck_rt.png'},
    'C1': {'type': 'car', 'height': 60, 'width': 60, 'image': 'car_1.png'},
    'C2': {'type': 'car', 'height': 60, 'width': 60, 'image': 'car_2.png'},
    'C3': {'type': 'car', 'height': 60, 'width': 60, 'image': 'car_3.png'},
    'D': {'type': 'dozer', 'height': 60, 'width': 60, 'image': 'dozer.png'},
    'GTL': {'type': 'grass', 'height': 60, 'width': 30, 'image': 'grass_tl.png'},
    'GTR': {'type': 'grass', 'height': 60, 'width': 30, 'image': 'grass_tr.png'},
    'GBR': {'type': 'grass', 'height': 60, 'width': 30, 'image': 'grass_br.png'},
    'GBL': {'type': 'grass', 'height': 60, 'width': 30, 'image': 'grass_bl.png'},
    'GMW': {'type': 'grass', 'height': 60, 'width': 30, 'image': 'grass_mw.png'},
    'GMT': {'type': 'grass', 'height': 60, 'width': 30, 'image': 'grass_mt.png'},
    'GMB': {'type': 'grass', 'height': 60, 'width': 30, 'image': 'grass_mb.png'},
}

IMAGES = {obj_type: pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_DIR, OBJECT_MAP[obj_type]['image'])), (OBJECT_MAP[obj_type]['width'], OBJECT_MAP[obj_type]['height'])) for obj_type in OBJECT_MAP}