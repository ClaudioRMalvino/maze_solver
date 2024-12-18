from cells import Cell
import time
import random


class Maze:
    """
    Constructs the maze in which the Cell objects will reside.
    """

    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        win=None,
        seed=None,
    ):

        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self.win = win

        self._cells = [
            [Cell(win=self.win) for j in range(self.num_rows)]
            for i in range(self.num_cols)
        ]

        if win != None:
            self._create_cells()
            self._break_entrance_and_exit()
            self._break_walls_r(0, 0)
            self._reset_cells_visited()

        if seed != None:
            random.seed(seed)

    def _create_cells(self):
        """
        Constructs all cells within the maze as a 2D array (list of lists).
        """

        for i in range(self.num_cols):
            for j in range(self.num_rows):

                self._draw_cell(i, j)

    def _draw_cell(self, i: int, j: int):
        """
        Draws cells onto the canvas at postion (cell_size_x*i, cell_size_y*j)

        Args:
            i (int): row number in self._cells()
            j (int): column number in self._cells()
        """
        if self.win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _break_entrance_and_exit(self):
        """
        Creates and entrance and exit for the maze solver to pass through.
        """

        # Creates the entrance to the maze
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        self._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)

    def _break_walls_r(self, i: int, j: int):
        """
        Method is a depth-first traversal through the cells, breaking down
        walls as it goes through each cell.

        Args:
            i (int): The column index
            j (int): The row index
        """

        self._cells[i][j].visited = True

        while True:
            to_visit = []

            # Check if the left cell has been visited
            if i > 0 and not self._cells[i - 1][j].visited:
                to_visit.append((i - 1, j))

            # Check if the right cell has been visited
            if i < self.num_cols - 1 and not self._cells[i + 1][j].visited:
                to_visit.append((i + 1, j))

            # Check if the below cell has been visited
            if j > 0 and not self._cells[i][j - 1].visited:
                to_visit.append((i, j - 1))

            # Check if the above cell has been visited
            if j < self.num_rows - 1 and not self._cells[i][j + 1].visited:
                to_visit.append((i, j + 1))

            # If there is nowhere else to go, break the loop
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return

            # Randomly choose the next direction to go

            direction = random.randrange(len(to_visit))
            next_index = to_visit[direction]

            # Knocks out the walls between the current cell and the adjacent ones

            # Knocks down right wall
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False

            # Knocks down left wall
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False

            # Knocks down bottom wall
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False

            # Knocks down top wall
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            # recursively visit the next cell
            self._break_walls_r(next_index[0], next_index[1])

    def _reset_cells_visited(self):
        """
        Resets all cells to visited = False
        """

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False

    def solve(self) -> bool:
        """
        Calls the recursive solve function and return true/false if the maze has been solved/not solved.

        Returns:
            bool: True if solved, False otherwise
        """

        return self._solve_r()

    def _solve_r(self, i=0, j=0) -> bool:
        """
        Utilized depth-frist search to travel along adjacent cells and solve the maze.

        Args:
            i (int, optional): Starting column index. Defaults to 0:int.
            j (int, optional): Starting row index. Defaults to 0:int.

        Returns:
            bool: True if solved, False otherwise
        """

        self._animate()
        self._cells[i][j].visited = True

        if (i == self.num_cols - 1) and (j == self.num_rows - 1):
            return True

        # Move left if there is no wall and it hasn't been visited
        if (
            i > 0
            and not self._cells[i][j].has_left_wall
            and not self._cells[i - 1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)

        # Move right if there is no wall and it hasn't been visited
        if (
            i < self.num_cols - 1
            and not self._cells[i][j].has_right_wall
            and not self._cells[i + 1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)

        # Move up if there is no wall and it hasn't been visited
        if (
            j > 0
            and not self._cells[i][j].has_top_wall
            and not self._cells[i][j - 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)

        # Move down if there is no wall and it hasn't been visited
        if (
            j < self.num_rows - 1
            and not self._cells[i][j].has_bottom_wall
            and not self._cells[i][j + 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)

        # We went the wrong way let the previous cell know by returning False
        return False

    def _animate(self):
        """
        Animates the action of the maze solver as it traverses the maze
        """

        self.win.redraw()
        time.sleep(0.05)
