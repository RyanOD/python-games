import pygame

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 1080
SCREEN_CAPTION = "Frogger Clone by Retro Clone"
SCREEN_BG = "assets/bg.png"

LANE_PADDING = 6
LANE_HEIGHT = 64
LANE_WIDTH = 64

ROAD_EDGE = 960

FROG_WIDTH = 24
FROG_HEIGHT = 24
FROG_MOVEMENT_X = 60
FROG_MOVEMENT_Y = 60
DEATH_TIMER = 50

BLUE = (0, 51, 153)
BLACK = (0, 0, 0)

OBJECT_MAP = {
    'F': {'type': 'frog', 'height': 50, 'width': 50, 'image': 'assets/frog_1.png'},
    'FD': {'type': 'frog', 'height': 60, 'width': 60, 'image': 'assets/dead_4.png'},
    'T': {'type': 'turtle', 'height': 60, 'width': 60, 'image': 'assets/turtle_1.png'},
    'LL': {'type': 'log', 'height': 60, 'width': 60, 'image': 'assets/log_lt.png'},
    'LM': {'type': 'log', 'height': 60, 'width': 60, 'image': 'assets/log_md.png'},
    'LR': {'type': 'log', 'height': 60, 'width': 60, 'image': 'assets/log_rt.png'},
    'TL': {'type': 'truck', 'height': 60, 'width': 60, 'image': 'assets/truck_lt.png'},
    'TR': {'type': 'truck', 'height': 60, 'width': 60, 'image': 'assets/truck_rt.png'},
    'C1': {'type': 'car', 'height': 60, 'width': 60, 'image': 'assets/car_1.png'},
    'C2': {'type': 'car', 'height': 60, 'width': 60, 'image': 'assets/car_2.png'},
    'C3': {'type': 'car', 'height': 60, 'width': 60, 'image': 'assets/car_3.png'},
    'D': {'type': 'dozer', 'height': 60, 'width': 60, 'image': 'assets/dozer.png'},
    'GTL': {'type': 'grass', 'height': 60, 'width': 30, 'image': 'assets/grass_tl.png'},
    'GTR': {'type': 'grass', 'height': 60, 'width': 30, 'image': 'assets/grass_tr.png'},
    'GBR': {'type': 'grass', 'height': 60, 'width': 30, 'image': 'assets/grass_br.png'},
    'GBL': {'type': 'grass', 'height': 60, 'width': 30, 'image': 'assets/grass_bl.png'},
    'GMW': {'type': 'grass', 'height': 60, 'width': 30, 'image': 'assets/grass_mw.png'},
    'GMT': {'type': 'grass', 'height': 60, 'width': 30, 'image': 'assets/grass_mt.png'},
    'GMB': {'type': 'grass', 'height': 60, 'width': 30, 'image': 'assets/grass_mb.png'},
}

IMAGES = {obj_type: pygame.transform.scale(pygame.image.load(OBJECT_MAP[obj_type]['image']), (OBJECT_MAP[obj_type]['width'], OBJECT_MAP[obj_type]['height'])) for obj_type in OBJECT_MAP}
print(IMAGES)