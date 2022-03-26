class Rectangle:
    """
    The Rectangle class takes origin co-ordinates(top-left corner),height, breadth and color as parameters and draws
    the rectangle on the Canvas.
    """

    def __init__(self, x, y, height, breadth, color):
        self.x = x
        self.y = y
        self.height = height
        self.breadth = breadth
        self.color = color

    def draw(self, canvas):
        """
            Draws itself onto the canvas
            :param canvas: canvas object is given as parameter
            :return: colour of the slice of the canvas is changed
        """
        canvas.data[self.x: self.x + self.height, self.y: self.y + self.breadth] = self.color


class Square:
    """
    The Square class takes origin co-ordinates(top-left corner), side and color as parameters and draws the
    square on the Canvas.
    """

    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        """
            Draws itself onto the canvas
            :param canvas: canvas object is given as parameter
            :return: colour of the slice of the canvas is changed
        """
        canvas.data[self.x: self.x + self.side, self.y: self.y + self.side] = self.color