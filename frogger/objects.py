from observer import Observable
from config import SCREEN_WIDTH

class Object(Observable):
    def __init__(self, type, images, x, y, movement):
        super().__init__()
        self.type = type
        self.image = images[type]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.movement = movement

    def update(self, dt):
        self.rect.x += round(self.movement * dt, 2)
        self.position_handler()
    
    def draw(self, screen):
        screen.surface.blit(self.image, self.rect)

    def position_handler(self):
        if self.rect.left > SCREEN_WIDTH:
            self.rect.right = 0
        elif self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH