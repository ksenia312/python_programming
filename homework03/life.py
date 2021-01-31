import pathlib
import random

from typing import List, Optional, Tuple

Cell = Tuple[int, int]
Cells = List[int]
Grid = List[Cells]


class GameOfLife:
    def __init__(
            self,
            size: Tuple[int, int],
            randomize: bool = True,
            max_generations: Optional[float] = float('inf')
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

    def create_grid(self, randomize: bool = True) -> Grid:
        if not randomize:
            grid1 = [[0 for i in range(self.cols)] for j in range(self.rows)]
        else:
            grid1 = [[random.randint(0, 1) for i in range(self.cols)] for j in range(self.rows)]
        return grid1

    def get_neighbours(self, cell: Cell) -> Cells:
        cells_cort = []
        cells = []
        h = cell[0]
        w = cell[1]
        if w - 1 >= 0:
            cells_cort.append((h, w - 1))
        if w + 1 < self.cols:
            cells_cort.append((h, w + 1))
        if h - 1 >= 0:
            cells_cort.append((h - 1, w))
        if h + 1 < self.rows:
            cells_cort.append((h + 1, w))
        if h - 1 >= 0 and w - 1 >= 0:
            cells_cort.append((h - 1, w - 1))
        if h - 1 >= 0 and w + 1 < self.cols:
            cells_cort.append((h - 1, w + 1))
        if h + 1 < self.rows and w - 1 >= 0:
            cells_cort.append((h + 1, w - 1))
        if h + 1 < self.rows and w + 1 < self.cols:
            cells_cort.append((h + 1, w + 1))
        for k in cells_cort:
            cells.append(self.curr_generation[k[0]][k[1]])
        return cells

    def get_next_generation(self) -> Grid:
        new_grid = []
        for i in range(self.rows):
            new_grid.append([])
            for j in range(self.cols):
                neighbours = self.get_neighbours((i, j))
                if sum(neighbours) == 3:
                    new_grid[i].append(1)
                elif self.curr_generation[i][j] == 1 and sum(neighbours) == 2:
                    new_grid[i].append(1)
                else:
                    new_grid[i].append(0)
        self.generations += 1
        return new_grid

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        self.prev_generation = self.curr_generation
        self.curr_generation = self.get_next_generation()

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        k = True
        if self.generations > self.max_generations:
            k = False
        return k

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        k = True
        if self.prev_generation == self.curr_generation:
            k = False
        return k

    @staticmethod
    def from_file(filename: pathlib.Path) -> 'GameOfLife':
        """
        Прочитать состояние клеток из указанного файла.
        """
        pass

    def save(filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        pass

'''
a = 1
while a != 0:
    game = GameOfLife((5, 5))
    grid = game.get_next_generation()
    a = game.get_neighbours((0, 0))
    print(grid)
'''