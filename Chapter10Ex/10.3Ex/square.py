class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Square(Rectangle):

    def __init__(self, side_length):
        super().__init__(side_length, side_length)

sq1 = Square(4)

print(sq1.area())

sq1.width = 5

print(sq1.area())

