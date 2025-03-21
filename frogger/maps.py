OBJECT_MAP = {
    'T': {'type': 'turtle', 'width': 60, 'height': 60, 'speed': 1.1, 'direction': 'left', 'image': 'assets/turtle_1.png'},
    'LL': {'type': 'log', 'width': 60, 'height': 60, 'speed': 1.4, 'direction': 'right', 'image': 'assets/log_lt.png'},
    'LM': {'type': 'log', 'width': 60, 'height': 60, 'speed': 1.4, 'direction': 'right', 'image': 'assets/log_md.png'},
    'LR': {'type': 'log', 'width': 60, 'height': 60, 'speed': 1.4, 'direction': 'right', 'image': 'assets/log_rt.png'},
    'C1': {'type': 'car', 'width': 60, 'height': 60, 'speed': 1.1, 'direction': 'left', 'image': 'assets/car_1.png'},
    'C2': {'type': 'car', 'width': 60, 'height': 60, 'speed': 1.5, 'direction': 'left', 'image': 'assets/car_2.png'},
    'C3': {'type': 'car', 'width': 60, 'height': 60, 'speed': 1.3, 'direction': 'right', 'image': 'assets/car_3.png'},
    'D': {'type': 'dozer', 'width': 60, 'height': 60, 'speed': 1.6, 'direction': 'right', 'image': 'assets/dozer.png'},
    'GTR': {'type': 'grass_top_right', 'width': 60, 'height': 60, 'speed': 0, 'direction': 'right', 'image': 'assets/grass_tr.png'},
    'GBM': {'type': 'grass_top_right', 'width': 60, 'height': 60, 'speed': 0, 'direction': 'right', 'image': 'assets/grass_bm.png'},
    'GTL': {'type': 'grass_top_right', 'width': 60, 'height': 60, 'speed': 0, 'direction': 'right', 'image': 'assets/grass_tl.png'},
    'GMM': {'type': 'grass_top_right', 'width': 60, 'height': 60, 'speed': 0, 'direction': 'right', 'image': 'assets/grass_mm.png'},
}

LEVEL_MAP = [
    [
        ['GTR', 'GBM', 'GTL', 'GMM', 'GTR', 'GBM', 'GTL', 'GMM', 'GTR', 'GBM', 'GTL', 'GMM','GTR', 'GBM', 'GTL', 'GMM',],
        ['', '', 'T', 'T', '', 'T', 'T', '', '', 'T', 'T', '', 'T', 'T'],
        ['LL', 'LM', 'LM', 'LM', 'LM', 'LR', '', '', 'LL', 'LM', 'LM', 'LM', 'LM', 'LR', ''],
        ['', 'LL', 'LM', 'LR', '', '', '', 'LL', 'LM', 'LR', '', '', '', 'LL', 'LM', 'LR'],
        ['T', 'T', 'T', '', 'T', 'T', 'T', '', 'T', 'T', 'T', '', 'T', 'T'],
        ['', '', '', '', '', '', '', '', '', '', '', '', '', ''],
        ['C3', '', '', '', '', '', '', '', '', '', '', '', '', ''],
        ['', '', '', 'C2', '', '', 'C2', '', '', 'C2', '', '', '', ''],
        ['', 'D', '', '', '', 'D', '', '', '', 'D', '', '', '', ''],
        ['', '', '', 'C1', '', '', 'C1', '', '', 'C1', '', '', 'C1', ''],
        ['', '', '', '', '', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ]
]