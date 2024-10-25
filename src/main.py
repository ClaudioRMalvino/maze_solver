from window import Window
from maze import Maze


def main():

    win = Window(800, 600)
    maze = Maze(0, 0, 4, 6, 30, 30, win=win)
    maze.solve()
    win.wait_for_close()


if __name__ == "__main__":

    main()
