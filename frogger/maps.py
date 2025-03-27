SCREEN_WIDTH = 900
SCREEN_HEIGHT = 1020

OBJECT_WIDTH = 60
OBJECT_HEIGHT = 60
OBJECTS_OFFSET = 240

LANE_PADDING = 4
LANE_HEIGHT = 60
LANE_WIDTH = 60

BLUE = (0, 51, 153)
BLACK = (0, 0, 0)

OBJECT_MAP = {
    'T': {'type': 'turtle', 'width': OBJECT_WIDTH, 'height': OBJECT_HEIGHT, 'image': 'assets/turtle_1.png'},
    'LL': {'type': 'log', 'width': OBJECT_WIDTH, 'height': OBJECT_HEIGHT, 'image': 'assets/log_lt.png'},
    'LM': {'type': 'log', 'width': OBJECT_WIDTH, 'height': OBJECT_HEIGHT, 'image': 'assets/log_md.png'},
    'LR': {'type': 'log', 'width': OBJECT_WIDTH, 'height': OBJECT_HEIGHT, 'image': 'assets/log_rt.png'},
    'TL': {'type': 'truck', 'width': OBJECT_WIDTH, 'height': OBJECT_HEIGHT, 'image': 'assets/truck_lt.png'},
    'TR': {'type': 'truck', 'width': OBJECT_WIDTH, 'height': OBJECT_HEIGHT, 'image': 'assets/truck_rt.png'},
    'C1': {'type': 'car', 'width': OBJECT_WIDTH, 'height': OBJECT_HEIGHT, 'image': 'assets/car_1.png'},
    'C2': {'type': 'car', 'width': OBJECT_WIDTH, 'height': OBJECT_HEIGHT, 'image': 'assets/car_2.png'},
    'C3': {'type': 'car', 'width': OBJECT_WIDTH, 'height': OBJECT_HEIGHT, 'image': 'assets/car_3.png'},
    'D': {'type': 'dozer', 'width': OBJECT_WIDTH, 'height': OBJECT_HEIGHT, 'image': 'assets/dozer.png'},
    'GTR': {'type': 'grass_top_right', 'width': OBJECT_WIDTH, 'height': OBJECT_HEIGHT, 'image': 'assets/grass_tr.png'},
    'GBM': {'type': 'grass_top_right', 'width': OBJECT_WIDTH, 'height': OBJECT_HEIGHT, 'image': 'assets/grass_bm.png'},
    'GTL': {'type': 'grass_top_right', 'width': OBJECT_WIDTH, 'height': OBJECT_HEIGHT, 'image': 'assets/grass_tl.png'},
    'GMM': {'type': 'grass_top_right', 'width': OBJECT_WIDTH, 'height': OBJECT_HEIGHT, 'image': 'assets/grass_mm.png'},
}

LEVEL_MAP = [
    [
        {
            'number': 1,
            'speed': 100,
            'direction': 'right',
            'objects': ['LL', 'LM', 'LM', 'LM', 'LR', '', '', 'LL', 'LM', 'LM', 'LM', 'LR', '', '', ''],
        },
        {
            'number': 2,
            'speed': 80,
            'direction': 'left',
            'objects': ['T', 'T', '', '', '', 'T', 'T', '', '', '', 'T', 'T', '', ''],
        },
        {
            'number': 3,
            'speed': 120,
            'direction': 'right',
            'objects': ['', 'LL', 'LM', 'LM', 'LM', 'LM', 'LR', '', '', 'LL', 'LM', 'LM', 'LM', 'LM', 'LR', ''],
        },
        {
            'number': 4,
            'speed': 110,
            'direction': 'right',
            'objects': ['LL', 'LM', 'LR', '', '', 'LL', 'LM', 'LR', '', '', 'LL', 'LM', 'LR', '', ''],
        },
        {
            'number': 5,
            'speed': 100,
            'direction': 'left',
            'objects': ['T', 'T', 'T', '', '', 'T', 'T', 'T', '', '', 'T', 'T', 'T', ''],
        },
        {
            'number': 6,
            'speed': 100,
            'direction': 'right',
            'objects': ['', '', '', '', '', '', '', '', '', '', '', '', '', ''],
        },
        {
            'number': 7,
            'speed': 80,
            'direction': 'left',
            'objects': ['', 'TL', 'TR', '', '', '', '', '', 'TL', 'TR', '', '', '', ''],
        },
        {
            'number': 8,
            'speed': 120,
            'direction': 'left',
            'objects': ['', '', '', 'C2', '', '', '', '', '', '', 'C2', '', '', ''],
        },
        {
            'number': 9,
            'speed': 100,
            'direction': 'right',
            'objects': ['', 'D', '', '', '', 'D', '', '', '', 'D', '', '', '', ''],
        },
        {
            'number': 10,
            'speed': 150,
            'direction': 'left',
            'objects': ['', '', '', 'C1', '', '', '', '', '', 'C1', '', '', '', ''],
        },
        {
            'number': 11,
            'speed': 90,
            'direction': 'right',
            'objects': ['', 'D', '', '', '', 'D', '', '', '', 'D', '', '', '', ''],
        },
        {
            'number': 12,
            'speed': 70,
            'direction': 'left',
            'objects': ['', '', 'C2', '', '', '', '', 'C2', '', '', '', '', '', ''],
        },
        {
            'number': 13,
            'speed': 140,
            'direction': 'right',
            'objects': ['', '', '', 'C3', '', '', '', '', 'C3', '', '', '', '', ''],
        },
    ]
]