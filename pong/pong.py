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

# define screen surface object
screen = Screen(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_PADDING)
surface = screen.surface
pygame.display.set_caption("Pong Clone")

# create instance of ball
ball = Ball(BALL_RADIUS, BALL_COLOR, SCREEN_WIDTH, SCREEN_HEIGHT)

# instantiate Clock instance and limit the game loop to 60 FPS
clock = pygame.time.Clock()

# instantiate two instances of Paddle class
paddle_lt = Paddle(SCREEN_PADDING, SCREEN_HEIGHT)
paddle_rt = Paddle(SCREEN_WIDTH - SCREEN_PADDING, SCREEN_HEIGHT)

running = True

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and ball.speed == 0:
            if event.key == pygame.K_p:
                ball.serve()
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        paddle_lt.move("up", screen)
    elif pressed[pygame.K_s]:
        paddle_lt.move("down", screen)

    screen.clear(FIELD_COLOR)
    screen.draw_line((255, 0, 0))
    ball.draw(surface)
    ball.move(screen)
    screen.boundary_check(ball)
    screen.passed(ball)
    ball.collision_check(paddle_lt, paddle_rt)
    paddle_lt.draw(surface)
    paddle_rt.draw(surface)
    screen.display_score()

    pygame.display.flip()
pygame.quit()