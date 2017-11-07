import math
import pygame


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mag(self):
        # Returns magnitude of the vector
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalise(self):
        # Normalises vector so magnitude is 1
        length = self.mag()
        if length > 0:
            self.x /= length
            self.y /= length

    def __add__(self, vector):
        Vector(self.x + vector.x, self.y + vector.y)

    def __sub__(self, vector):
        Vector(self.x - vector.x, self.y - vector.y)

    def __mul__(self, vector):
        if isinstance(vector, Vector):
            self.x *= vector.x
            self.y *= vector.y
        else:
            self.x *= vector
            self.y *= scalar

    def __iter__(self):
        yield self.x
        yield self.y
        
    def __eq__(self, vector):
        return self.x == vector.x and self.y == vector.y

    def __ne__(self, vector):
        return self.__eq__(vector)
        
    def __str__(self):
        return '(%.2f, %.2f)' % (self.x, self.y)