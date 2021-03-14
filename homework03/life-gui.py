import pygame
from pygame.locals import *

from life import GameOfLife
from ui import UI


class GUI():

    def __init__(self, life: GameOfLife, cell_size: int = 20, speed: int = 10) -> None:

        self.cell_size = cell_size
        self.speed = speed
        super().__init__()
        self.life = life
        self.screen_size = self.life.cols * self.cell_size, self.life.rows * self.cell_size
        self.screen = pygame.display.set_mode(self.screen_size)

    def draw_lines(self) -> None:
        for x in range(0, self.screen_size[0], self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('#889ac2'), (x, 0), (x, self.screen_size[1]))
        for y in range(0, self.screen_size[1], self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('#889ac2'), (0, y), (self.screen_size[0], y))

    def draw_grid(self) -> None:
        grid = self.life.curr_generation
        for i in range(self.life.rows):
            for j in range(self.life.cols):
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

    def runn(self) -> None:
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
            self.life.curr_generation = self.life.get_next_generation()

            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()


if __name__ == '__main__':
    game = GameOfLife((50, 50))
    g = GUI(game)

    g.runn()
