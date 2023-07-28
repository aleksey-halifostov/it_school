import math


class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def distance_from_origin(self):
        return math.hypot(self.x, self.y)


class Circle(Point):

    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __str__(self):
        return f'radius={self.radius} ' + super().__str__()

    def __add__(self, other):
        new = super().__add__(other)
        radius = self.radius + other.radius
        return Circle(radius, new.x, new.y)

    def edge_distance_from_origin(self):
        return abs(self.distance_from_origin() - self.radius)

    def circumference(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * (self.radius**2)

    def __sub__(self, other):
        new_object = Point(self.x - other.x, self.y - other.y)
        delta_radius = abs(self.radius - other.radius)

        if delta_radius:
            new_object = Circle(delta_radius, new_object.x, new_object.y)

        return new_object

