import pygame
from game import Game
from classes import *

# create instance of Game class
game = Game()

# instantiate instance of screen class and attach to surface
screen = Screen()
surface = screen.surface
pygame.display.set_caption("Pong Clone")

# create instance of Frog class
frog = Frog(screen)

while not game.game_over():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.lives = 0
    
    screen.draw()
    frog.draw(screen)

pygame.quit()