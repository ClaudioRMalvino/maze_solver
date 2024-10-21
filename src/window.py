from tkinter import Tk, BOTH, Canvas


class Window:

    def __init__(self, width, height):

        # Sets the width and height of our window
        self.width, self.height = width, height

        # Intializes our root_widget, the base of our app
        self.root_widget = Tk()
        self.root_widget.title("Maze Solver")

        # The object that we will draw on in our window
        # Outputing any images
        self.canvas = Canvas(self.root_widget,
                             width=self.width,
                             height=self.height)

        self.canvas.pack()

        self.window_running = False
        self.root_widget.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        """
        Will redraw and update the window as Tkinter is not a reactive
        framework.
        """

        self.root_widget.update_idletasks()
        self.root_widget.update()

    def draw_line(self, line, fill_color):
        """
        Draws a line utilizing the Line() object and it's draw() method
        """

        line.draw(self.canvas, fill_color)

    def wait_for_close(self):
        """
        Sets window_running to True and redraws our canvas while True
        """

        self.window_running = True
        while self.window_running:
            self.redraw()

    def close(self):
        """
        Sets window_running to False, closing the window
        """

        self.window_running = False
