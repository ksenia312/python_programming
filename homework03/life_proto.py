import pygame
from random import *
from pygame.locals import *
from typing import List, Tuple

Cell = Tuple[int, int]
Cells = List[int]
Grid = List[List[int]]


class GameOfLife:

    def __init__(self, width: int = 1000, height: int = 800, cell_size: int = 10, speed: int = 30) -> None:
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
        self.grid = self.create_grid(randomize=True)

    def run(self) -> None:
        """ Запустить игру """
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')

        self.screen.fill(pygame.Color('white'))
        # Создание списка клеток

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            # Отрисовка списка клеток

            self.draw_grid()
            self.draw_lines()
            # Выполнение одного шага игры (обновление состояния ячеек)
            self.grid = self.get_next_generation()

            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def draw_lines(self) -> None:
        """ Отрисовать сетку """
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('#889ac2'), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('#889ac2'), (0, y), (self.width, y))

    def create_grid(self, randomize: bool = True) -> Grid:
        """
        Создание списка клеток.

        Клетка считается живой, если ее значение равно 1, в противном случае клетка
        считается мертвой, то есть, ее значение равно 0.

        Parameters
        ----------
        randomize : bool
            Если значение истина, то создается матрица, где каждая клетка может
            быть равновероятно живой или мертвой, иначе все клетки создаются мертвыми.

        Returns
        ----------
        out : Grid
            Матрица клеток размером `cell_height` х `cell_width`.
        """
        if not randomize:
            grid = [[0 for i in range(self.cell_width)] for j in range(self.cell_height)]
        else:
            grid = [[randint(0, 1) for i in range(self.cell_width)] for j in range(self.cell_height)]
        return grid

    def draw_grid(self) -> None:
        """
        Отрисовка списка клеток с закрашиванием их в соответствующе цвета.
        """
        grid = self.grid
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                if grid[i][j] == 1:
                    pygame.draw.rect(
                        self.screen,
                        pygame.Color('#260d94'),
                        pygame.Rect(j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size)
                    )
                else:
                    pygame.draw.rect(
                        self.screen,
                        pygame.Color('white'),
                        pygame.Rect(j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size)
                    )

    def get_neighbours(self, cell: Cell) -> Cells:
        """
        Вернуть список соседних клеток для клетки `cell`.

        Соседними считаются клетки по горизонтали, вертикали и диагоналям,
        то есть, во всех направлениях.

        Parameters
        ----------
        cell: Cell
            Клетка, для которой необходимо получить список соседей. Клетка
            представлена кортежем, содержащим ее координаты на игровом поле.

        Returns
        ----------
        out : Cells
            Список соседних клеток.
        """
        cells_cort = []
        cells = []
        h = cell[0]
        w = cell[1]
        if w - 1 >= 0:
            cells_cort.append((h, w - 1))
        if w + 1 < self.cell_width:
            cells_cort.append((h, w + 1))
        if h - 1 >= 0:
            cells_cort.append((h - 1, w))
        if h + 1 < self.cell_height:
            cells_cort.append((h + 1, w))
        if h - 1 >= 0 and w - 1 >= 0:
            cells_cort.append((h - 1, w - 1))
        if h - 1 >= 0 and w + 1 < self.cell_width:
            cells_cort.append((h - 1, w + 1))
        if h + 1 < self.cell_height and w - 1 >= 0:
            cells_cort.append((h + 1, w - 1))
        if h + 1 < self.cell_height and w + 1 < self.cell_width:
            cells_cort.append((h + 1, w + 1))
        for k in cells_cort:
            cells.append(self.grid[k[0]][k[1]])
        return cells

    def get_next_generation(self) -> Grid:
        """
        Получить следующее поколение клеток.

        Returns
        ----------
        out : Grid
            Новое поколение клеток.
        """
        new_grid = []
        for i in range(self.cell_height):
            new_grid.append([])
            for j in range(self.cell_width):
                neighbours = self.get_neighbours((i, j))
                if sum(neighbours) == 3:
                    new_grid[i].append(1)
                elif self.grid[i][j] == 1 and sum(neighbours) == 2:
                    new_grid[i].append(1)
                else:
                    new_grid[i].append(0)

        return new_grid


if __name__ == '__main__':
    game = GameOfLife()
    game.run()
