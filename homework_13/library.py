from abc import ABC, abstractmethod
from math import sqrt


class Point:

    x = None
    y = None

    def __init__(self, val_x, val_y):
        self.x_descriptor = val_x
        self.y_descriptor = val_y

    @property
    def x_descriptor(self):
        return self.x

    @x_descriptor.setter
    def x_descriptor(self, value):
        if not type(value) in (int, float):
            raise TypeError

        self.x = value

    @property
    def y_descriptor(self):
        return self.x

    @y_descriptor.setter
    def y_descriptor(self, value):
        if not type(value) in (int, float):
            raise TypeError

        self.y = value


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

    begin = None
    end = None

    def __init__(self, begin_value, end_value):
        self.begin_descriptor = begin_value
        self.end_descriptor = end_value

    @property
    def begin_descriptor(self):
        return self.begin

    @begin_descriptor.setter
    def begin_descriptor(self, value):
        if not isinstance(value, Point):
            raise TypeError

        self.begin = value

    @property
    def end_descriptor(self):
        return self.end

    @end_descriptor.setter
    def end_descriptor(self, value):
        if not isinstance(value, Point):
            raise TypeError

        self.end = value

    def length(self):
        res = ((self.begin.x - self.end.x)**2 + (self.begin.y - self.end.y)**2)**0.5
        return res

    def area(self):
        pass


class Triangle(Figure):

    point1 = None
    point2 = None
    point3 = None

    def __init__(self, point1_value, point2_value, point3_value):
        self.point1_descriptor = point1_value
        self.point2_descriptor = point2_value
        self.point3_descriptor = point3_value
        self.lineA = Line(self.point1_descriptor, self.point2_descriptor).length()
        self.lineB = Line(self.point2_descriptor, self.point3_descriptor).length()
        self.lineC = Line(self.point3_descriptor, self.point1_descriptor).length()

    @property
    def point1_descriptor(self):
        return self.point1

    @point1_descriptor.setter
    def point1_descriptor(self, value):
        if not isinstance(value, Point):
            raise TypeError

        self.point1 = value

    @property
    def point2_descriptor(self):
        return self.point2

    @point2_descriptor.setter
    def point2_descriptor(self, value):
        if not isinstance(value, Point):
            raise TypeError

        self.point2 = value

    @property
    def point3_descriptor(self):
        return self.point3

    @point3_descriptor.setter
    def point3_descriptor(self, value):
        if not isinstance(value, Point):
            raise TypeError

        self.point3 = value

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError

        return self.area() == other.area()

    def __gt__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError

        return self.area() > other.area()

    def __ge__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError

        return self.area() >= other.area()

    def __str__(self):
        return f"{self.point1.x},{self.point1.y} -- {self.point2.x},{self.point2.y} -- {self.point3.x},{self.point3.y}"

    def length(self):
        result = self.lineA + self.lineB + self.lineC

        return result

    def area(self):
        semiperimeter = self.length() / 2
        result = sqrt(semiperimeter * (semiperimeter - self.lineA) * (semiperimeter - self.lineB)
                      * (semiperimeter - self.lineC))

        return result
