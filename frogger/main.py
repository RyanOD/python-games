import pygame
from game import Game
from classes import *

# instantiate instance of screen class and attach to surface
screen = Screen()
surface = screen.surface
pygame.display.set_caption("Frogger Clone")

# create instance of Game class
game = Game(screen)

while not game.game_over():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.lives = 0
        game.input_handler.handle_event(event)
    
    #game.input_handler.handle_input(pygame.key.get_pressed())

    game.draw()

pygame.quit()