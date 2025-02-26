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
ball = Ball(BALL_RADIUS, BALL_COLOR, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

# instantiate Clock instance and limit the game loop to 60 FPS
clock = pygame.time.Clock()
clock.tick(60)

# instantiate two instances of Paddle class
paddle_lt = Paddle(SCREEN_PADDING, SCREEN_HEIGHT / 2)
paddle_rt = Paddle(SCREEN_WIDTH - SCREEN_PADDING, SCREEN_HEIGHT / 2)

running = True

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
    
    if ball.x <= paddle_lt.x and ball.y > paddle_lt.y and ball.y < paddle_lt.y + paddle_lt.height:
        ball.speed_x *= -1
    if ball.x >= paddle_rt.x and ball.y > paddle_rt.y and ball.y < paddle_rt.y + paddle_rt.height:
        ball.speed_x *= -1

    screen.clear(FIELD_COLOR)
    screen.draw_line((255, 0, 0))
    ball.draw(surface)
    ball.move(screen)
    paddle_lt.draw(surface)
    paddle_rt.draw(surface)

    pygame.display.flip()
pygame.quit()