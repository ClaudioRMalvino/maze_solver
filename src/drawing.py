"""
Holds the classes utilized for drawing on the canvas

Point()
Line()
"""


class Point:

    def __init__(self, x, y):
        self.x = x      # Horizontal position in pixels
        self.y = y      # Vertical position in pixels


class Line:

    def __init__(self, point1, point2):

        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color: str):

        canvas.create_line(
            self.point1.x,
            self.point1.y,
            self.point2.x,
            self.point2.y,
            fill=fill_color,
            width=2
        )
