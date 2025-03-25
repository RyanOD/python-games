import pygame
from classes import *
from maps import *
from asset_paths import *

class Game:
    def __init__(self, level):
        pygame.init()  # Initialize Pygame
        self.clock = pygame.time.Clock()
        self.level = level
        self.lanes = self.get_lanes(LEVEL_MAP[self.level - 1])
        self.running = True
        self.playing = True
        self.hedge = pygame.transform.scale(pygame.image.load('assets/hedge.png'), (OBJECT_HEIGHT, OBJECT_WIDTH))
        self.lives = 3
        self.screen = Screen()
        self.surface = self.screen.surface
        self.frog = Frog(self.screen)
        self.input_handler = InputHandler(self.frog)
        self.collision_handler = CollisionHandler()
        self.sound_handler = SoundHandler()

    def get_lanes(self, level_data):
        lanes =[]
        for lane_data in level_data:
            lanes.append(Lane(lane_data))
        return lanes
    
    def update(self):
        for lane in self.lanes:
            self.collision_handler.check_collisions(self.frog, lane.objects)

    def draw(self):
        self.screen.reset()
        
        if self.hedge:
            for i in range(0, self.screen.width, OBJECT_WIDTH):
                self.screen.surface.blit(self.hedge, (i, 420))
                self.screen.surface.blit(self.hedge, (i, 900))

        for lane in self.lanes:
            for object in lane.objects:
                if object.image:
                    self.screen.surface.blit(object.image, (object.rect.x, object.rect.y))
                    pygame.draw.rect(self.screen.surface, (0, 0, 255), object.rect, 2)
                    

        if self.frog.image:
            self.screen.surface.blit(self.frog.image, (self.frog.rect.x, self.frog.rect.y))
            pygame.draw.rect(self.screen.surface, (255, 0, 0), self.frog.rect, 2)

        self.draw_grid()

        pygame.display.flip()

    def draw_grid(self):
        for i in range(0, self.screen.height, 60):
            pygame.draw.line(self.screen.surface, (255, 255, 255), (0, i), (self.screen.width, i))

        for i in range(0, self.screen.width, 60):
            pygame.draw.line(self.screen.surface, (255, 255, 255), (i, 0), (i, self.screen.height))

    def game_over(self):
        return self.lives <= 0
