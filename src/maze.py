"""
Contains the Maze class 
"""

import time
from cells import Cell


class Maze:
    """
    Constructs the Maze object, which will hold an array of Cell objects
    and draw them onto the canvas.
    """

    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None
    ):

        self.x1 = x1                        # Starting x position of our maze
        self.y1 = y1                        # Starting y position of our maze
        self.num_rows = num_rows            # Sets the # of rows for array
        self.num_cols = num_cols            # Sets the # of columns for array
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = [
            [Cell(self.cell_size_x,
                  self.cell_size_y,
                  self.cell_size_x,
                  self.cell_size_y,
                  win=self.win)

                for i in range(self.num_rows)
             ]
            for j in range(self.num_cols)
        ]

    def _create_cells(self):
        """
        Creates the array of Cell objects as a list of lists for our maze and then
        draws them utilizing the _draw_cell() method.
        """

        for i in range(self.num_rows):
            for j in range(self.num_cols):

                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        """
        Calculates the position of our cells given the maze's
        starting (x,y) position, the size of the cells, and their position 
        in the matrix.
        """

        x1 = self.x1 + i * self.cell_size_x
        y1 = self.x1 + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y

        cell = self._cells[i][j]
        cell.set_position(x1, y1, x2, y2)
        cell.draw()
        self._animate()

    def _animate(self):
        """
        Animates the maze by calling redraw(), sleeping for a period,
        and then calling redraw again.
        """

        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        """
        Removes the top wall from the entrance of the maze and removes the 
        bottom wall from the exit of the maze.
        """

        # The cell at point (x,y) at the start of the maze
        self._cells[0][0] = Cell(
            self.cell_size_x,
            self.cell_size_y,
            self.cell_size_x,
            self.cell_size_y,
            win=self.win,
            has_top_wall=False
        )

        self._cells[0][0].draw()

        # The cell at the bottome right corner of the maze
        self._cells[self.num_rows][self.num_cols] = Cell(
            self.cell_size_x,
            self.cell_size_y,
            self.cell_size_x,
            self.cell_size_y,
            win=self.win,
            has_bottom_wall=False)

        self._cells[self.num_rows][self.num_cols].draw()
