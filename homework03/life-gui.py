import argparse

import pygame
from pygame.locals import *

from life import GameOfLife
from ui import UI


class GUI(UI):

    def __init__(self, life: GameOfLife, cell_size: int = 20, speed: int = 10) -> None:

        super().__init__(life)

        self.cell_size = cell_size
        self.speed = speed
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

    def run(self) -> None:
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        # self.screen.fill(pygame.Color('white'))
        # Создание списка клеток
        running = True
        stop = False
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                if event.type == KEYDOWN:
                    stop = not stop
                if event.type == MOUSEBUTTONDOWN and stop:  # пауза при нажатии любой кнопки клавиатуры
                    y, x = pygame.mouse.get_pos()
                    self.life.curr_generation[x // self.cell_size][y // self.cell_size] = \
                        int(not self.life.curr_generation[x // self.cell_size][y // self.cell_size])
                    # Отрисовка списка клеток
                    self.draw_grid()
                    self.draw_lines()
                    pygame.display.flip()
            # Выполнение одного шага игры (обновление состояния ячеек)
            if not stop:
                self.life.curr_generation = self.life.get_next_generation()
                self.draw_grid()
                self.draw_lines()
                pygame.display.flip()
                clock.tick(self.speed)
        pygame.quit()


if __name__ == "__main__":
    ''''''
    parser = argparse.ArgumentParser(description="Let's play the Game of Life", prog="gof-gui.py")
    parser.add_argument('--width', type=int, default=640,
                        help='Enter width of window with game')
    parser.add_argument('--height', type=int, default=480,
                        help='Enter height of window with game')
    parser.add_argument('--cell_size', type=int, default=20,
                        help='Enter cell size')
    args = parser.parse_args()
    w = args.width > 0
    h = args.height > 0
    c = args.cell_size > 0
    if w and h and c and args.width // args.cell_size > 0 and args.height // args.cell_size > 0:
        gui = GUI(GameOfLife((args.width // args.cell_size, args.height // args.cell_size)), cell_size=args.cell_size)
        gui.run()
    else:
        print('The input received incorrect values. Try again please')
        if not w:
            print('Incorrect value of width')
        if not h:
            print('Incorrect value of height')
        if not c:
            print('Incorrect value of cell size')
