import argparse
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

        screen = curses.initscr()
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
        curses.endwin()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Let's play the Game of Life", prog="gof-console.py")
    parser.add_argument('--rows', type=int, default=24,
                        help='Enter count of rows(If you enter a value greater than 24, '
                             'an error may occur due to the too small size of your terminal window)')
    parser.add_argument('--cols', type=int, default=80,
                        help='Enter count of cols (If you enter a value greater than 80, '
                             'an error may occur due to the too small size of your terminal window)')
    parser.add_argument('--max_generations', type=int, default=50, help='Enter count of max generations')
    args = parser.parse_args()
    r = args.rows > 0
    c = args.cols > 0
    m = args.max_generations > 0
    if r and c and m:
        console = Console(GameOfLife((args.rows, args.cols), max_generations=args.max_generations))
        curses.update_lines_cols()
        console.run()
    else:
        print('The input received incorrect values. Try again please')
        if not r:
            print('Incorrect value of rows')
        if not c:
            print('Incorrect value of cols')
        if not m:
            print('Incorrect value of max generations')