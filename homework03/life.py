import pathlib
import random
from copy import deepcopy

from typing import List, Optional, Tuple
from random import randint 

Cell = Tuple[int, int]
Cells = List[int]
Grid = List[Cells]


class GameOfLife:
    
    def __init__(
        self,
        size: Tuple[int, int],
        randomize: bool=True,
        max_generations: Optional[float]=float('inf')
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
        self.generations = 1

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
        self.prev_generation = deepcopy(self.curr_generation)
        self.curr_generation = self.get_next_generation()
        self.generations += 1
        pass

    @property
    def is_max_generations_exceeded(self) -> bool:
        if self.generations > self.max_generations:
            return False
        else:
            return True

    @property
    def is_changing(self) -> bool:
        if self.prev_generation == self.curr_generation:
            return False
        else:
            return True

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

    def save(filename: pathlib.Path) -> None:
        with open(filename) as f:
            for i in range(len(self.curr_generation)):
                file.write(''.join(self.curr_generation[i]) + '/n')
        pass
        pass

    def save(filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        pass
