from canvas import Canvas
from shape import Rectangle, Square

# can = Canvas(200, 100, [255, 255, 255])
# r1 = Rectangle(10, 30, 120, 50, [255, 32, 165])
# r1.draw(can)
# s1 = Square(50, 20, 55, [55, 112, 65])
# s1.draw(can)
#
# can.make('image.png')
#
# color = {'black': [0, 0, 0], 'white': [255, 255, 255]}

while True:
    # Create canvas
    width = int(input("What width will have the canvas? "))
    height = int(input("What height will have the canvas? "))

    color = {'black': [0, 0, 0], 'white': [255, 255, 255]}
    # Select the color of canvas
    color_of_canvas = (color[input("Witch color (white or black) will have the canvas? ").lower()])

    # create a shape
    shape = input("which shape do you want to create (square or rectangle)? ")

    if shape == 'rectangle':
        x = int(input('What coordinate of x it have? '))
        y = int(input('What coordinate of y it have? '))
        shape_width = int(input("What width will have the rectangle? "))
        shape_height = int(input("What height will have the rectangle? "))

        print('We create a color of the rectangle. rgb')
        r = int(input("How mach red do you want? (0,255) "))
        g = int(input("How mach green do you want? (0,255) "))
        b = int(input("How mach blue do you want? (0,255) "))
        color = [r, g, b]

        shape = Rectangle(x, y, shape_width, shape_height, color)
    elif shape == 'square':
        x = int(input('What coordinate of x it have? '))
        y = int(input('What coordinate of y it have? '))
        shape_width = int(input("What length of side will have the square? "))

        print('We create a color of the square. rgb')
        r = int(input("How mach red do you want? (0,255) "))
        g = int(input("How mach green do you want? (0,255) "))
        b = int(input("How mach blue do you want? (0,255) "))
        color = [r, g, b]

        shape = Square(x, y, shape_width, color)

    # create a img with shapes
    canvas = Canvas(width, height, color_of_canvas)
    # draw the shape on canvas
    shape.draw(canvas)
    # create file cli_image.png with canvas and shapes on them
    canvas.make('files/cli_image.png')

    answer = input('Do you wont to create another figure? y/n: ')
    if answer.lower() == 'n':
        print('Bye')
        break
