"""
Cell class is used to construct the cells within the canvas.
It is the unit distances we can traverse within the maze and we 
can travel through a cell as long as it does not have walls in the direction
of motion.
"""


class Cell:

    def __init__(self,
                 x1, x2, y1, y2, win,
                 has_left_wall=True,
                 has_right_wall=True,
                 has_top_wall=True,
                 has_bottom_wall=True,
                 ):

        # Public Variables
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win

    def draw(self):
        """
        Draws a cell, where each wall being drawn is dependent
        on if it is set to True.
        """

        if self.has_left_wall:
            self._win.canvas.create_line(
                self._x1,
                self._y1,
                self._x1,
                self._y2,
                fill="black",
                width=1
            )

        if self.has_right_wall:
            self._win.canvas.create_line(
                self._x2,
                self._y1,
                self._x2,
                self._y2,
                fill="black",
                width=1
            )
        if self.has_top_wall:
            self._win.canvas.create_line(
                self._x1,
                self._y2,
                self._x2,
                self._y2,
                fill="black",
                width=1
            )

        if self.has_bottom_wall:
            self._win.canvas.create_line(
                self._x1,
                self._y1,
                self._x2,
                self._y1,
                fill="black",
                width=1
            )

    def draw_move(self, to_cell, undo=False):
        """
        Draws a path between 2 cells. It draws a line from the center
        one cell to another.
        """

        self_center = ((self._x2 + self._x1) // 2, (self._y2 + self._y1) // 2)
        cell2_center = ((to_cell._x2 + to_cell._x1)//2,
                        (to_cell._y2 + to_cell._y1)//2)

        if undo:

            self._win.canvas.create_line(
                self_center[0],
                self_center[1],
                cell2_center[0],
                cell2_center[1],
                fill="gray",
                width=2

            )
        self._win.canvas.create_line(
            self_center[0],
            self_center[1],
            cell2_center[0],
            cell2_center[1],
            fill="gray",
            width=2

        )
