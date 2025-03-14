import pygame
from classes import *
from levels import *
from asset_paths import *

class Game:
    def __init__(self):
        pygame.init()  # Initialize Pygame
        self.current_level = None
        self.running = True
        self.playing = True
        self.hedge_road = pygame.transform.scale(pygame.image.load('assets/hedge_road.png'), (60, 60))
        self.hedge_water = pygame.transform.scale(pygame.image.load('assets/hedge_water.png'), (60, 60))
        #self.car_1 = pygame.image.load('assets/car_1.png')
        self.lives = 3
        self.screen = Screen()
        self.surface = self.screen.surface
        self.objects = []
        self.frog = Frog(self.screen)
        self.input_handler = InputHandler(self.frog)

    def update(self):
        pass

    def load_level(self, level):
        self.objects_data = LEVELS[level - 1]
        
        for i, lane in enumerate(self.objects_data):
            for j, object in enumerate(lane):
                if object == 'T':
                    self.objects.append(GameObject('turtle', 60, 60, 1, j * 80, i * 80, 'left', ASSET_DIRECTORY + '/' + CAR_1_IMG))
                #elif object == 'LL':
                 #   self.objects.append(GameObject('log_left', 60, 60, 1, j * 40, i * 40, 'left', image))
                #elif object == 'LR':
                 #   self.objects.append(GameObject('log_right', 60, 60, 1, j * 40, i * 40, 'left', image))
                #elif object == 'LM':
                 #   self.objects.append(GameObject('log_middle', 60, 60, 1, j * 40, i * 40, 'left', image))
                elif object == 'C1':
                    self.objects.append(GameObject('car_1', 60, 60, 1, j * 80, i * 80, 'left', ASSET_DIRECTORY + '/' + CAR_1_IMG))
                elif object == 'C2':
                    self.objects.append(GameObject('car_2', 60, 60, 1, j * 80, i * 80, 'left', ASSET_DIRECTORY + '/' + CAR_2_IMG))
                elif object == 'C3':
                    self.objects.append(GameObject('car_3', 60, 60, 1, j * 80, i * 80, 'left', ASSET_DIRECTORY + '/' + CAR_3_IMG))
                elif object == 'D':
                    self.objects.append(GameObject('dozer', 60, 60, 1, j * 80, i * 80, 'left', ASSET_DIRECTORY + '/' + DOZER_IMG))

    def draw(self):
        self.screen.clear()
        pygame.display.set_caption("Frogger Clone")
        if self.hedge_water and self.hedge_road:
            for i in range(0, self.screen.width, 60):
                self.screen.surface.blit(self.hedge_water, (i, 410))
                self.screen.surface.blit(self.hedge_road, (i, 890))

        if self.frog.image:
            self.screen.surface.blit(self.frog.image, (self.frog.x, self.frog.y))
            #self.screen.surface.blit(self.car_1, (self.car_1.x, self.car_1.y))

        for object in self.objects:
            print(object)
            self.screen.surface.blit(object.image, (object.x, object.y))

        for i in range(0, self.screen.height, 80):
            pygame.draw.line(self.screen.surface, (255, 255, 255), (0, i), (self.screen.width, i))

        pygame.display.set_caption(self.screen.title)
        pygame.display.flip()

    def game_over(self):
        return self.lives <= 0
