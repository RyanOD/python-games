import pygame

class Screen:
    def __init__(self):
        self.width = 1200
        self.height = 800
        self.padding = 10
        self.color = (0, 0, 0)
        self.line_color = (255, 255, 255)
        self.player_score = 0
        self.pc_score = 0
        self.surface = pygame.display.set_mode((self.width, self.height))

    def title_screen(self):
        pass

    def clear(self, color):
        self.surface.fill(color)
    
    def draw_line(self, color):
        pygame.draw.line(self.surface, self.line_color, (self.width / 2 -  1, 0), (self.width / 2 - 1, self.height), 2)
    
    def boundary_check(self, ball):
        # collision detection with top and bottom walls
        if ball.y + ball.radius + self.padding >= self.height or ball.y - ball.radius - self.padding <= 0:
            ball.speed_y *= -1
    
    def passed(self, ball):
        if ball.x < -ball.radius:
            self.pc_score += 1
            ball.reset(self)
        elif ball.x > self.width + ball.radius:
            self.player_score += 1
            ball.reset(self)

    def display_score(self):
        font = pygame.font.Font(None, 74)
        player_score = font.render(str(self.player_score), True, (77, 77, 77))
        pc_score = font.render(str(self.pc_score), True, (77, 77, 77))
        self.surface.blit(player_score, (self.width / 4, self.padding))
        self.surface.blit(pc_score, (self.width * 3 / 4, self.padding))
