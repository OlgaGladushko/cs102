import pygame
import random
import math

from pygame.locals import *
from typing import List, Tuple
from random import randint 


Cell = Tuple[int, int]
Cells = List[int]
Grid = List[Cells]


class GameOfLife:

    def __init__(self, width: int=640, height: int=480, cell_size: int=10, speed: int=10) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed

    def draw_lines(self) -> None:
        """ Отрисовать сетку """
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                    (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                    (0, y), (self.width, y))

    def run(self) -> None:
        """ Запустить игру """
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))
        self.create_grid(True)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_lines()

            # Отрисовка списка клеток
            self.draw_grid()
            # Выполнение одного шага игры (обновление состояния ячеек)
            self.get_next_generation()
            # PUT YOUR CODE HERE
            
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def create_grid(self, randomize: bool=False) -> Grid:
        self.grid = []
        for height in range(self.cell_height):
            self.grid.append([])
            for width in range(self.cell_width):
                if randomize == False:
                    self.grid[height].append(0)
                else:
                    self.grid[height].append(randint(0, 1))
        return self.grid
	    
	    
    
    def draw_grid(self) -> None:
        for height in range(self.cell_height):
            for width in range(self.cell_width):
                x = height * self.cell_size
                y = width * self.cell_size
                a = self.cell_size
                if self.grid[height][width] == 0:
                    pygame.draw.rect(self.screen, pygame.Color('white'), (x, y, a, a))
                else:
                    pygame.draw.rect(self.screen, pygame.Color('green'), (x, y, a, a))
        pass

    def get_neighbours(self, cell: Cell) -> Cells:
        height = cell[0]
        width = cell[1] 
        Cells = []
        for i in range(height - 1, height + 2):
            for j in range(width - 1, width + 2):
                if (i != height or j != width) and (i in range(0, self.cell_height)) and (j in range(0, self.cell_width)):
                    Cells.append(self.grid[i][j])
        return Cells

    def get_next_generation(self) -> Grid:
        new_grid = []
        for height in range(self.cell_height):
            new_grid.append([])
            for width in range(self.cell_width):
                cond = self.grid[height][width]
                neig = self.get_neighbours((height, width))
                if neig.count(1) == 3 or (neig.count(1) == 2 and cond == 1):
                    new_grid[height].append(1)
                else:
                    new_grid[height].append(0)
        self.grid = new_grid            
        return self.grid
        

game = GameOfLife(900, 900, 9)
game.run()
