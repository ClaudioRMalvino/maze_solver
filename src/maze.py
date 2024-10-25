"""
Contains the Maze class
"""

import time
import random
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
        win=None,
        seed=None
    ):

        self.x1 = x1                        # Starting x position of our maze
        self.y1 = y1                        # Starting y position of our maze
        self.num_rows = num_rows            # Sets the # of rows for array
        self.num_cols = num_cols            # Sets the # of columns for array
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win                      # provides a window class to draw

        # Constructs the cells for the maze
        self._cells = [
            [Cell(self.cell_size_x,
                  self.cell_size_y,
                  self.cell_size_x,
                  self.cell_size_y,
                  win=self.win)

                for column in range(self.num_cols)
             ]
            for rows in range(self.num_rows)
        ]

        if seed is not None:
            self.seed = random.seed(seed)
        else:
            self.seed = seed

        self._create_cells()
        self._break_walls_r(0, 0)
        self._break_entrance_and_exit()

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
        y1 = self.y1 + j * self.cell_size_y
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
        self._cells[0][0].has_top_wall = False

        self._cells[0][0].draw()

    # The cell at the bottome right corner of the maze
        self._cells[self.num_rows-1][self.num_cols-1].has_bottom_wall = False
        print(self._cells[self.num_rows-1][self.num_cols-1])
        self._cells[self.num_rows-1][self.num_cols-1].draw()

    # def _break_walls_r(self, i, j):
    #     """
    #     A depth-first traversal method through the cells, breaking down the
    #     walls as it goes through.
    #     """
    #     def _break_adjacent_walls(i, j, next_i, next_j):
    #         """
    #         Helper function implements the breaking of walls
    #         to facilitate visiting the adjacent cell.
    #         """
    #
    #         if next_i > i and next_j == j:
    #             self._cells[i][j].has_right_wall = False
    #             self._cells[next_i][j].has_left_wall = False
    #         if next_i < i and next_j == j:
    #             self._cells[i][j].has_left_wall = False
    #             self._cells[next_i][j].has_right_wall = False
    #         if next_j > j and next_i == i:
    #             self._cells[i][j].has_top_wall = False
    #             self._cells[i][next_j].has_bottom_wall = False
    #         if next_j < j and next_i == i:
    #             self._cells[i][j].has_bottom_wall = False
    #             self._cells[i][next_j].has_top_wall = False
    #
    #     self._cells[i][j].visited = True
    #
    #     if i == self.num_rows - 1 and j == self.num_cols - 1:
    #         print("Visited exit cell")
    #     while True:
    #
    #         index_to_visit = []
    #         if i + 1 < len(self._cells) and not self._cells[i+1][j].visited:
    #             index_to_visit.append((i+1, j))
    #         if i - 1 >= 0 and not self._cells[i-1][j].visited:
    #             index_to_visit.append((i-1, j))
    #         if j + 1 < len(self._cells[0]) and not self._cells[i][j+1].visited:
    #             index_to_visit.append((i, j+1))
    #         if j - 1 >= 0 and not self._cells[i][j-1].visited:
    #             index_to_visit.append((i, j-1))
    #
    #         if not index_to_visit:
    #             return
    #
    #         rand_index = random.randrange(len(index_to_visit))
    #         next_i, next_j = index_to_visit.pop(rand_index)
    #
    #         _break_adjacent_walls(i, j, next_i, next_j)
    #
    #         self._break_walls_r(next_i, next_j)
    #
    def _break_walls_r(self, i, j):
        """
         A depth-first traversal method through the cells, breaking down the
         walls as it goes through.
         """
        def _break_adjacent_walls(i, j, next_i, next_j):
            if next_i > i and next_j == j:
                self._cells[i][j].has_right_wall = False
                self._cells[next_i][j].has_left_wall = False
                self._cells[i][j].draw()        # Redraw the current cell
                self._cells[next_i][j].draw()   # Redraw the next cell
            if next_i < i and next_j == j:
                self._cells[i][j].has_left_wall = False
                self._cells[next_i][j].has_right_wall = False
                self._cells[i][j].draw()
                self._cells[next_i][j].draw()
            if next_j > j and next_i == i:
                self._cells[i][j].has_top_wall = False
                self._cells[i][next_j].has_bottom_wall = False
                self._cells[i][j].draw()
                self._cells[i][next_j].draw()
            if next_j < j and next_i == i:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][next_j].has_top_wall = False
                self._cells[i][j].draw()
                self._cells[i][next_j].draw()

        self._cells[i][j].visited = True
        self._animate()  # Add animation for visualization

        while True:
            index_to_visit = []
            if i + 1 < len(self._cells) and not self._cells[i+1][j].visited:
                index_to_visit.append((i+1, j))
            if i - 1 >= 0 and not self._cells[i-1][j].visited:
                index_to_visit.append((i-1, j))
            if j + 1 < len(self._cells[0]) and not self._cells[i][j+1].visited:
                index_to_visit.append((i, j+1))
            if j - 1 >= 0 and not self._cells[i][j-1].visited:
                index_to_visit.append((i, j-1))
            if not index_to_visit:
                self._cells[i][j].draw()  # Ensure final cell is drawn
                return

            rand_index = random.randrange(len(index_to_visit))
            next_i, next_j = index_to_visit.pop(rand_index)

            _break_adjacent_walls(i, j, next_i, next_j)
            self._break_walls_r(next_i, next_j)

    def _reset_cells_visited(self):

        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._cells[i][j].visited = False

    # def solve(self):
    #
    #     self._reset_cells_visited()
    #     return self._solve_r(0, 0)
    #
    # def _solve_r(self, i, j):
    #     print(f"Current: ({i},{j}), Target: ({
    #           self.num_rows-1},{self.num_cols-1}), Visited: {self._cells[i][j].visited}")
    #     print(f"visiting cell ({i},{j})")
    #
    #     print(f"Cell ({i},{j}) walls: top={self._cells[i][j].has_top_wall}, right={
    #           self._cells[i][j].has_right_wall}, left={self._cells[i][j].has_left_wall}, bottom={self._cells[i][j].has_bottom_wall}")
    #
    #     self._animate()
    #     self._cells[i][j].visited = True
    #
    #     if i == self.num_rows-1 and j == self.num_cols-1:
    #         print(f"Checking if current cell ({i},{j}) is end cell ({
    #               self.num_rows-1},{self.num_cols-1})")
    #         return True
    #
    #     if (j + 1 < len(self._cells[0])) and not self._cells[i][j].has_right_wall and not self._cells[i][j+1].visited:
    #
    #         self._cells[i][j].draw_move(self._cells[i][j+1])
    #         if self._solve_r(i, j+1):
    #             return True
    #         else:
    #             self._cells[i][j+1].draw_move(self._cells[i][j], undo=True)
    #
    #     if (j - 1 >= 0) and not self._cells[i][j].has_left_wall and not self._cells[i][j-1].visited:
    #         self._cells[i][j].draw_move(self._cells[i][j-1])
    #         if self._solve_r(i, j-1):
    #             return True
    #         else:
    #             self._cells[i][j-1].draw_move(self._cells[i][j], undo=True)
    #
    #     if (i + 1 < len(self._cells)) and not self._cells[i][j].has_bottom_wall and not self._cells[i+1][j].visited:
    #
    #         self._cells[i][j].draw_move(self._cells[i+1][j])
    #         if self._solve_r(i+1, j):
    #             return True
    #         else:
    #             self._cells[i+1][j].draw_move(self._cells[i][j], undo=True)
    #
    #     if (i - 1 >= 0) and not self._cells[i][j].has_top_wall and not self._cells[i-1][j].visited:
    #
    #         self._cells[i][j].draw_move(self._cells[i-1][j])
    #         if self._solve_r(i-1, j):
    #             return True
    #         else:
    #             self._cells[i-1][j].draw_move(self._cells[i][j], undo=True)
    #
    #     print("made it to False")
    #     return False

    def _solve_r(self, i, j):
        """
        Recursive depth-first search maze solver with better backtracking.
        """
        # Mark cell as visited before checking anything else
        self._cells[i][j].visited = True
        self._animate()

        print(f"Current: ({i},{j}), Target: ({
              self.num_rows-1},{self.num_cols-1})")
        print(f"Cell ({i},{j}) walls: top={self._cells[i][j].has_top_wall}, right={self._cells[i][j].has_right_wall}, "
              f"left={self._cells[i][j].has_left_wall}, bottom={self._cells[i][j].has_bottom_wall}")

        # Check if we've reached the target
        if i == self.num_rows-1 and j == self.num_cols-1:
            print(f"Found end cell at ({i},{j})")
            return True

        # Store possible moves to try
        possible_moves = []

        # Check all possible moves and store valid ones
        # Check right
        if (j + 1 < self.num_cols and
            not self._cells[i][j].has_right_wall and
                not self._cells[i][j+1].visited):
            possible_moves.append((i, j+1, "right"))

        # Check bottom
        if (i + 1 < self.num_rows and
            not self._cells[i][j].has_bottom_wall and
                not self._cells[i+1][j].visited):
            possible_moves.append((i+1, j, "bottom"))

        # Check left
        if (j - 1 >= 0 and
            not self._cells[i][j].has_left_wall and
                not self._cells[i][j-1].visited):
            possible_moves.append((i, j-1, "left"))

        # Check top
        if (i - 1 >= 0 and
            not self._cells[i][j].has_top_wall and
                not self._cells[i-1][j].visited):
            possible_moves.append((i-1, j, "top"))

        print(f"Possible moves from ({i},{j}): {
              [move[2] for move in possible_moves]}")

        # Try each possible move
        for next_i, next_j, direction in possible_moves:
            print(f"Trying to move {direction} from ({
                  i},{j}) to ({next_i},{next_j})")
            self._cells[i][j].draw_move(self._cells[next_i][next_j])

            if self._solve_r(next_i, next_j):
                return True

            print(f"Backtracking from ({next_i},{next_j}) to ({i},{j})")
            self._cells[next_i][next_j].draw_move(self._cells[i][j], undo=True)

        print(f"No valid path found from ({i},{j}), backtracking")
        return False

    def solve(self):
        """
        Public solve method that resets visited cells and starts the recursive solve.
        """
        self._reset_cells_visited()

        # Add debugging for initial state
        print("\nStarting maze solve...")
        print(f"Maze dimensions: {self.num_rows}x{self.num_cols}")
        print(f"Target cell: ({self.num_rows-1},{self.num_cols-1})")

        result = self._solve_r(0, 0)

        if result:
            print("\nMaze solved!")
        else:
            print("\nNo solution found!")

        return result
