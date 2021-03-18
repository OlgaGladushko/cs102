import pathlib
import random
from random import randint
import typing as tp
from copy import deepcopy
import curses

import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:

    def __init__(
        self,
        size: tp.Tuple[int, int],
        randomize: bool=True,
        max_generations: tp.Optional[float]=float('inf')
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.n_generation = 1

    def create_grid(self, randomize: bool=False) -> Grid:
        grid = []
        for height in range(self.rows):
            grid.append([])
            for width in range(self.cols):
                if randomize == False:
                    grid[height].append(0)
                else:
                    grid[height].append(randint(0, 1))
        return grid

    def get_neighbours(self, cell: Cell) -> Cells:
        height = cell[0]
        width = cell[1] 
        Cells = []
        for i in range(height - 1, height + 2):
            for j in range(width - 1, width + 2):
                if (i != height or j != width) and (i in range(0, self.rows)) and (j in range(0, self.cols)):
                    Cells.append(self.curr_generation[i][j])
        return Cells

    def get_next_generation(self) -> Grid:
        new_grid = []
        for height in range(self.rows):
            new_grid.append([])
            for width in range(self.cols):
                cond = self.curr_generation[height][width]
                neig = self.get_neighbours((height, width))
                if neig.count(1) == 3 or (neig.count(1) == 2 and cond == 1):
                    new_grid[height].append(1)
                else:
                    new_grid[height].append(0)
        self.curr_generation = new_grid            
        return self.curr_generation

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        self.prev_generation = deepcopy(self.curr_generation)
        self.curr_generation = self.get_next_generation()
        self.n_generation += 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        if self.n_generation >= self.max_generations:
            return True
        else:
            return False

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        if self.curr_generation != self.prev_generation:
            return True
        else:
            return False

    @staticmethod
    def from_file(filename: pathlib.Path) -> 'GameOfLife':
        array = []
        with open(filename) as f:
            line = filename.readline()
            while line:
                array.append(line.list())
        self.curr_generation = array
        life = GameOfLife((len(array[0], len(array))))     
        return life

    def save(self, filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        f = open(filename, 'w')
        for row in self.curr_generation:
            for ch in row:
                f.write(''.join(str(ch)) + '\n')
        f.close()
