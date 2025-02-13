from winreg import KEY_CREATE_SUB_KEY

import pygame
from enum import Enum
import random


class ShapeType(Enum):
    I = 1
    J = 2
    L = 3
    O = 4
    S = 5
    T = 6
    Z = 7


class Shape:
    def __init__(self, shape_type: ShapeType, grid: list, gridSize: list, screen, hasCollided=False):
        self.shape_type = shape_type
        self.hasCollided = hasCollided
        self.grid = grid
        self.screen = screen

        self.states = self.get_rotation_states()
        self.current_state = self.states[random.randint(0, len(self.states) - 1)]
        self.gridPosition = [int(gridSize[1] / 2) - len(self.current_state[0]) / 2, 0]
        self.shapeBlock = pygame.Rect(self.gridPosition[0] * 20, self.gridPosition[1] * 20, 20, 20)
        self.get_color()
        self.current_rotation = 0
        self.rotation_states = self.get_rotation_states()

        self.placeShapeInGrid()

    def rotate(self):
        self.current_rotation = (self.current_rotation + 1) % len(self.rotation_states)

    def update(self):
        if (self.hasCollided):
            return

        if (self.gridPosition[1] <= len(self.grid) - len(self.current_state) + 1):
            
            # for i in range(len(self.grid)):
            #     for j in range(len(self.grid)):
            #         # self.collisionCheck(self.grid[i][j])
            #         # print(self.gridPosition)
            #         # print()

            self.gridPosition[1] += 1
            self.shapeBlock.x = self.gridPosition[0] * 20
            self.shapeBlock.y = self.gridPosition[1] * 20

        else:
            self.hasCollided = True

        self.move()

        pygame.display.flip()
        pygame.time.delay(100)

    def move(self):
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_LEFT] and not self.hasCollided):
            if (self.gridPosition[0] - 1 >= 0) :
                self.gridPosition[0] = int(self.gridPosition[0] - 1)

        if (keys[pygame.K_RIGHT] and not self.hasCollided):
            if (self.gridPosition[0] + 1 <= len(self.grid) - len(self.current_state)) :
                self.gridPosition[0] = int(self.gridPosition[0] + 1)

        if (keys[pygame.K_UP]):
            if (self.states.index(self.current_state) == len(self.states) - 1):
                self.current_state = self.states[0]
            else:
                self.current_state = self.states[self.states.index(self.current_state) + 1]

    def render(self):
        for i in range(len(self.current_state)):
            for j in range(len(self.current_state[0])):
                if self.current_state[i][j] == 1:
                    pygame.draw.rect(self.screen, self.get_color(),
                                     pygame.Rect(self.gridPosition[0] * 20 + j * 20, self.gridPosition[1] * 20 + i * 20,
                                                 20, 20))

    def placeShapeInGrid(self):
        for i in range(len(self.current_state)):
            for j in range(len(self.current_state[0])):
                if self.current_state[i][j] == 1:
                    self.grid[int(i + self.gridPosition[1])][int(j + self.gridPosition[0])] = 1

    def get_color(self):
        colors = {
            ShapeType.I: (0, 255, 255),  # Cyan
            ShapeType.O: (255, 255, 0),  # Yellow
            ShapeType.T: (128, 0, 128),  # Purple
            ShapeType.S: (0, 255, 0),  # Green
            ShapeType.Z: (255, 0, 0),  # Red
            ShapeType.J: (0, 0, 255),  # Blue
            ShapeType.L: (255, 165, 0),  # Orange
        }
        return colors[self.shape_type]

    def get_rotation_states(self):
        states = {
            ShapeType.I: [
                [[1, 1, 1, 1]],
                [[1], [1], [1], [1]]
            ],
            ShapeType.O: [
                [[1, 1],
                 [1, 1]]
            ],
            ShapeType.T: [
                [[0, 1, 0],
                 [1, 1, 1]],
                [[1, 0],
                 [1, 1],
                 [1, 0]],
                [[1, 1, 1],
                 [0, 1, 0]],
                [[0, 1],
                 [1, 1],
                 [0, 1]],
            ],
            ShapeType.S: [
                [[0, 1, 1],
                 [1, 1, 0]],
                [[1, 0],
                 [1, 1],
                 [0, 1]],
            ],
            ShapeType.Z: [
                [[1, 1, 0],
                 [0, 1, 1]],
                [[0, 1],
                 [1, 1],
                 [1, 0]],
            ],
            ShapeType.J: [
                [[1, 0, 0],
                 [1, 1, 1]],
                [[1, 1],
                 [1, 0],
                 [1, 0]],
                [[1, 1, 1],
                 [0, 0, 1]],
                [[0, 1],
                 [0, 1],
                 [1, 1]],
            ],
            ShapeType.L: [
                [[0, 0, 1],
                 [1, 1, 1]],
                [[1, 0],
                 [1, 0],
                 [1, 1]],
                [[1, 1, 1],
                 [1, 0, 0]],
                [[1, 1],
                 [0, 1],
                 [0, 1]],
            ]
        }
        return states[self.shape_type]

    def get_grid(self):
        return self.grid

    def get_screen(self):
        return pygame.display.get_surface()
