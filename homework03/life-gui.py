import pygame
from pygame.locals import *

from life import GameOfLife
from ui import UI


class GUI(UI):

    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 10) -> None:
        self.cell_size = cell_size
        self.speed = speed
        super().__init__(life)

    def draw_lines(self) -> None:
        for x in range(0, self.cols, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('#889ac2'), (x, 0), (x, self.rows))
        for y in range(0, self.rows, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('#889ac2'), (0, y), (self.cols, y))

    def draw_grid(self) -> None:
        grid = self.curr_generation
        for i in range(self.self.rows):
            for j in range(self.self.cols):
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

    def run(self) -> None:
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

            self.draw_grid()
            self.draw_lines()
            # Выполнение одного шага игры (обновление состояния ячеек)
            self.curr_generation = self.get_next_generation()

            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()


if __name__ == '__main__':
    game = GUI((5, 5))
    game.run()
