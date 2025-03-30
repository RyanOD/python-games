import pygame

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 1020
SCREEN_CAPTION = "Frogger Clone by Retro Clone"

OBJECT_WIDTH = 60
OBJECT_HEIGHT = 60
OBJECTS_OFFSET = 240

LANE_PADDING = 0
LANE_HEIGHT = 64
LANE_WIDTH = 64

BLUE = (0, 51, 153)
BLACK = (0, 0, 0)

OBJECT_MAP = {
    'F': {'type': 'frog', 'image': 'assets/frog_1.png'},
    'FD': {'type': 'frog', 'image': 'assets/dead_4.png'},
    'T': {'type': 'turtle', 'image': 'assets/turtle_1.png'},
    'LL': {'type': 'log', 'image': 'assets/log_lt.png'},
    'LM': {'type': 'log', 'image': 'assets/log_md.png'},
    'LR': {'type': 'log', 'image': 'assets/log_rt.png'},
    'TL': {'type': 'truck', 'image': 'assets/truck_lt.png'},
    'TR': {'type': 'truck', 'image': 'assets/truck_rt.png'},
    'C1': {'type': 'car', 'image': 'assets/car_1.png'},
    'C2': {'type': 'car', 'image': 'assets/car_2.png'},
    'C3': {'type': 'car', 'image': 'assets/car_3.png'},
    'D': {'type': 'dozer', 'image': 'assets/dozer.png'},
    'GTR': {'type': 'grass_top_right', 'image': 'assets/grass_tr.png'},
    'GBM': {'type': 'grass_top_right', 'image': 'assets/grass_bm.png'},
    'GTL': {'type': 'grass_top_right', 'image': 'assets/grass_tl.png'},
    'GMM': {'type': 'grass_top_right', 'image': 'assets/grass_mm.png'},
}

IMAGES = {obj_type: pygame.transform.scale(pygame.image.load(OBJECT_MAP[obj_type]['image']), (OBJECT_HEIGHT, OBJECT_WIDTH)) for obj_type in OBJECT_MAP}


LEVEL_MAP = [
    [
        {
            'movement': 230,
            'objects': ['LL', 'LM', 'LM', 'LM', 'LR', '', '', 'LL', 'LM', 'LM', 'LM', 'LR', '', '', ''],
        },
        {
            'movement': -90,
            'objects': ['T', 'T', '', '', '', 'T', 'T', '', '', '', 'T', 'T', '', ''],
        },
        {
            'movement': 115,
            'objects': ['', 'LL', 'LM', 'LM', 'LM', 'LM', 'LR', '', '', 'LL', 'LM', 'LM', 'LM', 'LM', 'LR', ''],
        },
        {
            'movement': 80,
            'objects': ['LL', 'LM', 'LR', '', '', 'LL', 'LM', 'LR', '', '', 'LL', 'LM', 'LR', '', ''],
        },
        {
            'movement': -60,
            'objects': ['T', 'T', 'T', '', '', 'T', 'T', 'T', '', '', 'T', 'T', 'T', ''],
        },
        {
            'movement': 70,
            'objects': ['', '', '', '', '', '', '', '', '', '', '', '', '', ''],
        },
        {
            'movement': -60,
            'objects': ['', 'TL', 'TR', '', '', '', '', '', 'TL', 'TR', '', '', '', ''],
        },
        {
            'movement': -90,
            'objects': ['', '', '', 'C2', '', '', '', '', '', '', 'C2', '', '', ''],
        },
        {
            'movement': 80,
            'objects': ['', 'D', '', '', '', 'D', '', '', '', 'D', '', '', '', ''],
        },
        {
            'movement': -110,
            'objects': ['', '', '', 'C1', '', '', '', '', '', 'C1', '', '', '', ''],
        },
        {
            'movement': 50,
            'objects': ['', 'D', '', '', '', 'D', '', '', '', 'D', '', '', '', ''],
        },
        {
            'movement': -70,
            'objects': ['', '', 'C2', '', '', '', '', 'C2', '', '', '', '', '', ''],
        },
        {
            'movement': 110,
            'objects': ['', '', '', 'C3', '', '', '', '', 'C3', '', '', '', '', ''],
        },
    ]
]