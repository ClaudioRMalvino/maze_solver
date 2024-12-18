from drawing import Point, Line


class Cell:
    """
    The cell class holds the object of a cell, which is defined by having
    walls (or not) and its position on the canvas.

    The maze solver will traverse these cells, depending on the its walls.
    """

    def __init__(self, win=None):

        # Initializes position on canvas
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None

        # Initializes the window so that can access the canvas
        self._win = win

        # Initializes the walls of the Cell
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        # Indicates if the maze solver has visited the cell
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        """
        Draws a cell on the canvas depending on the cells structure

        Ex: (has_left_wall=True, has_right_wall=False,
        has_top_wall=False, has_bottom_wall=True)

        Will draw a unit cell with three walls with its top
        left corner at (_x1,y1) and bottom right corner at (x2,y2)
        """
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        top_left = Point(self._x1, self._y1)
        top_right = Point(self._x2, self._y1)
        bottom_left = Point(self._x1, self._y2)
        bottom_right = Point(self._x2, self._y2)

        fill_color_true = "black"  # Color for walls when True
        fill_color_false = "white"  # Colors for walls when False
        canvas = self._win.canvas

        # Draws left wall
        if self.has_left_wall:
            Line(top_left, bottom_left).draw(canvas, fill_color_true)
        else:
            Line(top_left, bottom_left).draw(canvas, fill_color_false)

        # Draws top wall
        if self.has_top_wall:
            Line(top_left, top_right).draw(canvas, fill_color_true)
        else:
            Line(top_left, top_right).draw(canvas, fill_color_false)

        # Draws bottom wall
        if self.has_bottom_wall:
            Line(bottom_left, bottom_right).draw(canvas, fill_color_true)
        else:
            Line(bottom_left, bottom_right).draw(canvas, fill_color_false)

        # Draws right wall
        if self.has_right_wall:
            Line(top_right, bottom_right).draw(canvas, fill_color_true)
        else:
            Line(top_right, bottom_right).draw(canvas, fill_color_false)

    def draw_move(self, to_cell: object, undo=False):
        """
        Draws a line from the center of the cell
        to the center of another to_cell.

        If undo=False, the line is red, else it is gray. This is to demonstrate
        the maze solvers movement, where gray demonstrates that it is
        backtracking.

        Args:
            to_cell (object): The adjacent cell to which the solver is moving
            undo (bool, optional): Checks if the maze is backtracking.
                                Defaults to False.
        """

        canvas = self._win.canvas

        self_center = Point((self._x2 + self._x1) // 2, (self._y2 + self._y1) // 2)

        to_cell_center = Point(
            (to_cell._x2 + to_cell._x1) // 2, (to_cell._y2 + to_cell._y1) // 2
        )

        if undo:
            fill_color = "gray"
            Line(self_center, to_cell_center).draw(canvas, fill_color)
        else:
            fill_color = "red"
            Line(self_center, to_cell_center).draw(canvas, fill_color)

    def __str__(self):

        return f"Cell[x1: {self._x1}, y1: {self._y1}, x2: {self._x2}, y2: {self._y2}]"
