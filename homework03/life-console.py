import curses
from life import GameOfLife
from ui import UI
from time import sleep
import sys
import argparse


class Console(UI):

    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)

    def draw_borders(self, screen) -> None:
        screen.border('|', '|', '-', '-', '+', '+', '+', '+')

    def draw_grid(self, screen) -> None:
        for i in range(1, self.life.rows):
            for j in range(1, self.life.cols):
                if self.life.curr_generation[i][j] == 1:
                    screen.addstr(j, i, '*')
                elif self.life.curr_generation[i][j] == 0:
                    screen.addstr(j, i, ' ')

    def run(self) -> None:
        screen = curses.initscr()
        while (self.life.is_max_generations_exceeded is False) and (self.life.is_changing is True):
            screen.clear()
            self.draw_borders(screen)
            self.draw_grid(screen)
            screen.refresh()
            sleep(1)
            self.life.step()
        screen.refresh()
        curses.endwin()
        
 
def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-c', '--cols', type=int, default=10)
    parser.add_argument ('-r', '--rows', type=int, default=10)
    parser.add_argument ('-m', '--max_generations', type=int, default=30)
    return parser
 
 
if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
 
    gui = Console(GameOfLife((namespace.cols, namespace.rows), True, namespace.max_generations))
    gui.run()
