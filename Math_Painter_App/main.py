from canvas import Canvas
from shapes import Rectangle, Square


# Get the canvas direction from
canvas_height = int(input("Please enter the required height of the canvas: "))
canvas_width = int(input("Please enter the required width of the canvas: "))
colors = {"white": (255, 255, 255), "black": (0, 0, 0)}
canvas_color = input("Please enter the required color of the canvas (black or white): ").lower()

# creating the canvas
canvas = Canvas(canvas_height, canvas_width, colors[canvas_color])

while True:
    # taking user-input for the shape
    shape = input("What would you like to draw today? To quit enter quit \n square or rectangle?: ").lower()
    # taking additional information for drawing a rectangle
    if shape == 'rectangle':
        rec_x = int(input("Enter the x co-ordinates of the rectangle: "))
        rec_y = int(input("Enter the y co-ordinates of the rectangle: "))
        rec_height = int(input("Enter the height of the rectangle: "))
        rec_width = int(input("Enter the width of the rectangle: "))
        rec_red = int(input("How much red should the rectangle have (0-255): "))
        rec_green = int(input("How much green should the rectangle have (0-255): "))
        rec_blue = int(input("How much much blue should the rectangle have (0-255): "))
        rectangle1 = Rectangle(rec_x, rec_y, rec_height, rec_width, (rec_red, rec_green, rec_blue))
        rectangle1.draw(canvas)
    # taking additional information for drawing a square
    elif shape == 'square':
        sq_x = int(input("Enter the x co-ordinates of the square: "))
        sq_y = int(input("Enter the y co-ordinates of the square: "))
        sq_side = int(input("Enter the side of the square: "))
        sq_red = int(input("How much red should the square have (0-255): "))
        sq_green = int(input("How much green should the square have (0-255): "))
        sq_blue = int(input("How much much blue should the square have (0-255): "))
        square1 = Square(sq_x, sq_y, sq_side, (sq_red, sq_green, sq_blue))
        square1.draw(canvas)
    if shape == 'quit':
        break
    canvas.make('canvas.png')
