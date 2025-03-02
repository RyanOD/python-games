import pygame
from game import Game
from screen import Screen
from ball import Ball
from paddle import Paddle
from input_handler import InputHandler

# instantiate instance of Game class
game = Game()

# instantiate instance of screen class and attach to surface
screen = Screen()
surface = screen.surface
pygame.display.set_caption("Pong Clone")

# instantiate instance of Ball class
ball = Ball(screen.width, screen.height)

# instantiate two instances of Paddle class
paddle_lt = Paddle(screen.padding, screen.height)
paddle_rt = Paddle(screen.width - screen.padding, screen.height)

# instantiate instance of InputHandler class
input_handler = InputHandler(paddle_lt, screen, ball, game)

# instantiate Clock instance and limit the game loop to 60 FPS
clock = pygame.time.Clock()

running = True

while running:
    clock.tick(60)
    for event in pygame.event.get():                
        pressed = pygame.key.get_pressed()
        input_handler.handle_input(pressed)

    screen.clear(screen.color)
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