import pygame
from paddle import Paddle

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_PADDING = 10
FIELD_COLOR = (0, 0, 0)
LINE_COLOR = (255, 255, 255)
BALL_COLOR = (255, 255, 255)
BALL_RADIUS = 10

# pygame setup
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

pygame.display.set_caption("Pong Clone")
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
            paddle_lt.move("up")
        elif event.key == pygame.K_s:
            paddle_lt.move("down")

    screen.fill(FIELD_COLOR)

    line = pygame.draw.line(screen, LINE_COLOR, (SCREEN_WIDTH / 2 -  1, 0), (SCREEN_WIDTH / 2 - 1, SCREEN_HEIGHT), 2)
    ball = pygame.draw.circle(screen, BALL_COLOR, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), BALL_RADIUS)

    paddle_lt = Paddle(SCREEN_PADDING, SCREEN_HEIGHT / 2)
    paddle_lt.render(screen)
    paddle_rt = Paddle(SCREEN_WIDTH - SCREEN_PADDING, SCREEN_HEIGHT / 2)
    paddle_rt.render(screen)

  pygame.display.flip()
pygame.quit()