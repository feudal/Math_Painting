class Rectangle:

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height

    def draw(self, canvas):
        canvas.data[self.y: self.y + self.height, self.x: self.x + self.width] = self.color


class Square:

    def __init__(self, x, y, width, color):
        self.x = x
        self.y = y
        self.width = width
        self.color = color

    def draw(self, canvas):
        canvas.data[self.y: self.y + self.width, self.x: self.x + self.width] = self.color


class Triangle:

    def __init__(self, x1, y1, x2, y2, x3, y3, color):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.color = color

    def draw(self, canvas):
        canvas.data[self.y1 - 1:self.y1, self.x1 - 1:self.x1] = self.color
        canvas.data[self.y2 - 1:self.y2, self.x2 - 1:self.x2] = self.color
        canvas.data[self.y3 - 1:self.y3, self.x3 - 1:self.x3] = self.color


