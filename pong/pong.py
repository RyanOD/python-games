import pygame

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
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
  
  screen.fill(FIELD_COLOR)

  line = pygame.draw.line(screen, LINE_COLOR, (SCREEN_WIDTH / 2 -  1, 0), (SCREEN_WIDTH / 2 - 1, SCREEN_HEIGHT), 2)
  ball = pygame.draw.circle(screen, BALL_COLOR, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), BALL_RADIUS)

  pygame.display.flip()
pygame.quit()