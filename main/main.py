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


# shape = Shape(random.choice(list(ShapeType)), grid, [len(grid), len(grid[0])], screen)

shapes = [Shape(random.choice(list(ShapeType)), grid, [len(grid), len(grid[0])], screen)]

print(shapes[0])

def update():
    if shapes[len(shapes) - 1].hasCollided:
        shapes.append(Shape(random.choice(list(ShapeType)), grid, [len(grid), len(grid[0])], screen))

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    for i in range(len(shapes)):
        shapes[i].render()
        shapes[i].update()

    update()

    screen = shapes[len(shapes) - 1].get_screen()
    pygame.display.update()

pygame.quit()