import math


N = ord('A') % 3 + 1
print(N)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"(x = {self.x}, y = {self.y})"

class WrongDataError(Exception):

    def __init__(self):
        super().__init__("This points create a degenerate triangle")


class  MissingParameterError(Exception):

    def __init__(self):
         super().__init__("Missing parameter")


class Triangle:

    def __init__(self, point1 = 0, point2 = 0, point3 = 0):
        self.vertices = [point1, point2, point3]


        if point1 == 0 or point2 == 0 or point3 == 0:
            raise MissingParameterError()

        if self.area() == 0:
            raise WrongDataError()




    def area(self):
        a = math.sqrt((self.vertices[1].x - self.vertices[0].x) ** 2 + (self.vertices[1].y - self.vertices[0].y) ** 2)
        b = math.sqrt((self.vertices[2].x - self.vertices[1].x) ** 2 + (self.vertices[2].y - self.vertices[1].y) ** 2)
        c = math.sqrt((self.vertices[2].x - self.vertices[0].x) ** 2 + (self.vertices[2].y - self.vertices[0].y) ** 2)
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area

    def perimeter(self):
        a = math.sqrt((self.vertices[1].x - self.vertices[0].x) ** 2 + (self.vertices[1].y - self.vertices[0].y) ** 2)
        b = math.sqrt((self.vertices[2].x - self.vertices[1].x) ** 2 + (self.vertices[2].y - self.vertices[1].y) ** 2)
        c = math.sqrt((self.vertices[2].x - self.vertices[0].x) ** 2 + (self.vertices[2].y - self.vertices[0].y) ** 2)
        return round(a + b + c, 3)


    def __str__(self) -> str:
        return f"A = {self.vertices[0]}" f" B = {self.vertices[1]}" f" C = {self.vertices[2]}"


triangle = Triangle(Point(-3, 6),Point(-3, 2))

print(triangle)
print(triangle.area())
print(triangle.perimeter())

