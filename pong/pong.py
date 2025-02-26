import pygame
from paddle import Paddle
from screen import Screen
from ball import Ball

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_PADDING = 10
FIELD_COLOR = (0, 0, 0)
LINE_COLOR = (255, 255, 255)
BALL_RADIUS = 10
BALL_COLOR = (255, 255, 255)

# pygame setup
pygame.init()

screen = Screen(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_PADDING)
surface = screen.surface

ball = Ball(BALL_RADIUS, BALL_COLOR, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

clock = pygame.time.Clock()
running = True

paddle_lt = Paddle(SCREEN_PADDING, SCREEN_HEIGHT / 2)
paddle_rt = Paddle(SCREEN_WIDTH - SCREEN_PADDING, SCREEN_HEIGHT / 2)

pygame.display.set_caption("Pong Clone")
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w] and paddle_lt.y > paddle_lt.height / 2 + SCREEN_PADDING:
        paddle_lt.move("up")
    elif pressed[pygame.K_s] and paddle_lt.y < SCREEN_HEIGHT - paddle_lt.height / 2 - SCREEN_PADDING:
        paddle_lt.move("down")
    elif pressed[pygame.K_p]:
        ball.serve()

    screen.clear(FIELD_COLOR)
    screen.draw_line((255, 0, 0))
    ball.draw(surface)
    ball.move(screen)
    paddle_lt.draw(surface)
    paddle_rt.draw(surface)

    pygame.display.flip()
pygame.quit()