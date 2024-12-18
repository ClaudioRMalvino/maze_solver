class Point:
    """
    Point object with an (x, y) coordinate position for placing draw
    objects on the canvas.
    """

    def __init__(self, x: int, y: int):

        # x_pos = 0 is the left of the canvas
        self.x_pos = x

        # y_pos = 0 is the top of the canvas
        self.y_pos = y


class Line:
    """
    Line object which is drawn onto the canvas.
    Takes two Point objects as input.
    """

    def __init__(self, point1: object, point2: object):

        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas: object, fill_color: str):
        """
        Takes a Canvas object and fill color as input and then draws
        the Line from point1 -> point2.
        """
        # The (x,y) position of point1
        x_pos1 = self.point1.x_pos
        y_pos1 = self.point1.y_pos

        # The (x,y) position of point2
        x_pos2 = self.point2.x_pos
        y_pos2 = self.point2.y_pos

        canvas.create_line(x_pos1, y_pos1, x_pos2, y_pos2, fill=fill_color, width=2)
