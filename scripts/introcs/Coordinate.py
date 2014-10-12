__author__ = 'nunoe'

import math


class Coordinate(object):
    """ Class used to represent coordinates in a 2-dimensional space """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'

    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


if __name__ == '__main__':

    origin = Coordinate(0, 0)
    c = Coordinate(5, 6)

    print 'Origin: ', origin
    print 'Point c: ', c
    print 'The distance between both points is: ' + str(c.distance(origin))

    print 'c is an instance of Coordinate: ' + str(isinstance(c, Coordinate))