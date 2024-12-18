from tkinter import Tk, BOTH, Canvas


class Window:
    """
    Window class constructs a window with which to contain the maze.
    """

    def __init__(self, width: int, height: int):

        # Sets the width and height of our window
        self.width = width
        self.height = height

        # Initializes our root_widget, the base of our app
        self.root_widget = Tk()
        self.root_widget.title("Maze Solver")

        # The object we will be drawing our maze onto
        self.canvas = Canvas(self.root_widget, width=self.width, height=self.height)

        self.canvas.pack(fill=BOTH, expand=True)

        self.window_running = False
        self.root_widget.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        """
        Will redraw and update the window as Tkinter is not a reactive
        framework.
        """

        self.root_widget.update_idletasks()
        self.root_widget.update()

    def draw_line(self, line: object, fill_color: str):
        """
        Draws a Line object onto the canvas with a given fill color.

        Args:
            line (object): Line object with two points
            fill_color (str): Color to draw the line in
        """

        line.draw(canvas=self.canvas, fill_color=fill_color)

    def wait_for_close(self):
        """
        Keep the window open as long as self.window_running is set to True.
        """

        self.window_running = True
        while self.window_running:
            self.redraw()

    def draw_text(self, text, x, y, color="black", size=20):
        """
        Draws text on the canvas at specified coordinates

        Args:
            text (str): Text to display
            x (int): x-coordinate for text position
            y (int): y-coordinate for text position
            color (str): Color of the text (default: green)
            size (int): Font size (default: 20)
        """
        self.canvas.create_text(
            x, y, text=text, fill=color, font=("Arial", size, "bold")
        )

    def close(self):
        """
        Sets self.window_running to False in order to close the window.
        """

        self.window_running = False
