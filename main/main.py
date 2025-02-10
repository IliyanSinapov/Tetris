import pygame
import random

from utilities import Shape, ShapeType

pygame.init()

SCREEN_DIMENSIONS = [800, 600]

screen = pygame.display.set_mode(SCREEN_DIMENSIONS)
pygame.display.set_caption("Tetris")

grid = [
    [0 for _ in range(10)] for _ in range(20)
]


shape = Shape(random.choice(list(ShapeType)), grid, [len(grid), len(grid[0])], screen)

grid = shape.get_grid()

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    shape.render()
    shape.update()

    screen = shape.get_screen()
    pygame.display.update()

pygame.quit()