class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return (self.height*2) + (self.width*2)

rect = Rectangle(4, 5)
print(rect.area())
print(rect.perimeter())