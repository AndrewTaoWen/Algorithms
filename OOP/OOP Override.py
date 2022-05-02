# from Point import Point

class Point:

    def __init__(self, x_cor=0, y_cor=0):
        self.x = x_cor
        self.y = y_cor

    def __str__(self):
        return f'Point ({self.x}, {self.y})'

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return self.__add__(other * -1)

    def distance(self, other):
        diff_x = other.x - self.x
        diff_y = other.y - self.y
        result = (diff_x ** 2 + diff_y ** 2) * 0.5
        return result


origin = Point()
f = Point(5, 12)
print(origin.distance(f))

a = Point(3, 5)
b = Point(7, 10)

point_list = [a, b]
print(point_list)

c = a + b
print(c)

