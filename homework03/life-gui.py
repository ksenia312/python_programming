import pygame
from pygame.locals import *

from life import GameOfLife
from ui import UI


class GUI(UI):

    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 10) -> None:
        self.cell_size = cell_size
        self.speed = speed
        super().__init__(life)

    def draw_lines(self, life) -> None:
        for x in range(0, life.cols, self.cell_size):
            pygame.draw.line(life.screen, pygame.Color('#889ac2'), (x, 0), (x, life.rows))
        for y in range(0, life.rows, self.cell_size):
            pygame.draw.line(life.screen, pygame.Color('#889ac2'), (0, y), (life.cols, y))

    def draw_grid(self, life) -> None:
        grid = life.curr_generation
        for i in range(life.rows):
            for j in range(life.cols):
                if grid[i][j] == 1:
                    pygame.draw.rect(
                        life.screen,
                        pygame.Color('#260d94'),
                        pygame.Rect(j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size)
                    )
                else:
                    pygame.draw.rect(
                        life.screen,
                        pygame.Color('white'),
                        pygame.Rect(j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size)
                    )

    def runn(self, life) -> None:
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        # self.screen.fill(pygame.Color('white'))
        # Создание списка клеток
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            # Отрисовка списка клеток

            self.draw_grid(life)
            self.draw_lines(life)
            # Выполнение одного шага игры (обновление состояния ячеек)
            life.curr_generation = life.get_next_generation()

            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()
