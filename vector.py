import math
import pygame as pg


class Vector():
    # NOTE: this is not our code, credit to pacmancode.com/vectors. This is only used for movement.
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.thresh = 0.000001

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __div__(self, scalar):
        if scalar != 0:
            return Vector(self.x / float(scalar), self.y/float(scalar))
        return None

    def __truediv__(self, scalar):
        return self.__div__(scalar)

    def __eq__(self, other):
        if abs(self.x - other.x) < self.thresh:
            if abs(self.y - other.y) < self.thresh:
                return True
        return False

    def magnitudeSquared(self):
        return self.x**2 + self.y**2

    def magnitude(self):
        return math.sqrt(self.magnitudeSquared())

    def copy(self):
        return Vector(self.x + self.y)

    def asTuple(self):
        return self.x, self.y

    def asInt(self):
        return int(self.x), int(self.y)

    def __str__(self):
        return "<" + str(self.x) + ", " + str(self.y) + ">"
