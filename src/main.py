from window import Window
from drawing import Point, Line
from cells import Cell


def main():

    win = Window(800, 600)
    point1 = Point(40, 40)
    point2 = Point(80, 80)

    line = Line(point1, point2)
    win.draw_line(line, "red")

    cell1 = Cell(200, 300, 200, 300, win=win)
    cell1.draw()
    cell2 = Cell(400, 300, 400, 300, win=win)
    cell2.draw()

    cell1.draw_move(cell2)
    win.wait_for_close()


if __name__ == "__main__":

    main()
