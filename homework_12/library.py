from abc import ABC, abstractmethod
from math import sqrt


class Point:

    def __init__(self, x, y):
        if type(x) in (int, float) and type(y) in (int, float):
            self.x = x
            self.y = y
        else:
            raise TypeError


class Figure(ABC):

    @abstractmethod
    def __init__(self):
        pass

    # @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def length(self):
        pass


class Line(Figure):

    def __init__(self, begin, end):
        if type(begin) is Point and type(end) is Point:
            self.begin = begin
            self.end = end
        else:
            raise TypeError

    def length(self):
        res = ((self.begin.x - self.end.x)**2 + (self.begin.y - self.end.y)**2)**0.5
        return res

    def area(self):
        pass


class Triangle(Figure):

    def __init__(self, point1, point2, point3):
        if type(point1) is Point and type(point2) is Point and type(point3) is Point:
            self.point1 = point1
            self.point2 = point2
            self.point3 = point3
            self.lineA = Line(point1, point2).length()
            self.lineB = Line(point2, point3).length()
            self.lineC = Line(point3, point1).length()
        else:
            raise TypeError

    def length(self):
        result = self.lineA + self.lineB + self.lineC

        return result

    def area(self):
        semiperimeter = self.length() / 2
        result = sqrt(semiperimeter * (semiperimeter - self.lineA) * (semiperimeter - self.lineB)
                      * (semiperimeter - self.lineC))

        return result
