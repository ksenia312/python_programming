import curses
import time
from life import GameOfLife
from ui import UI


class Console(UI):

    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)

    def draw_borders(self, screen) -> None:
        """ Отобразить рамку. """
        screen.border(0)

    def draw_grid(self, screen) -> None:
        """ Отобразить состояние клеток. """
        for i in range(1, len(self.life.curr_generation) - 1):
            for j in range(1, len(self.life.curr_generation[i]) - 1):
                if self.life.curr_generation[i][j]:
                    elem = "*"
                else:
                    elem = " "
                screen.addch(i, j, elem)

    def run(self) -> None:

        screen = curses.initscr().derwin(len(self.life.curr_generation), len(self.life.curr_generation[0]), 0, 0)
        curses.curs_set(0)
        running = True
        while running:
            screen.clear()
            self.draw_borders(screen)
            self.draw_grid(screen)
            self.life.step()
            if not self.life.is_max_generations_exceeded or not self.life.is_changing:
                running = False
            screen.refresh()
            time.sleep(0.2)

        #screen.getch()
        curses.endwin()


if __name__ == '__main__':
    life = GameOfLife((24, 80), max_generations=50)
    ui = Console(life)
    ui.run()
