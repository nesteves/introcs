__author__ = 'nunoe'


def f(t):
    """ Computes the amount of radiation emitted in MBq
        at time t

    :param t: int, point in time
    :return: float, the amount of radiation emitted during t
    """
    import math
    return 10 * math.e ** (math.log(0.5) / 5.27 * t)


def radiationExposure(start, stop, step):
    """ Computes the total amount of radiation exposure
        accumulated between an interval of time
    :param start: int, point in time where the radiation exposure begins
    :param stop: int, point int time where the radiation exposure ends
    :param step: width of the rectangle used to approximate the radiation
        exposure
    :return: float, the total radiation exposure in MBq
    """
    import numpy
    return sum([step * f(i) for i in numpy.arange(start, stop, step)])


if __name__ == '__main__':
    print 'Radiation exposure between point 0 and 5: ' + str(radiationExposure(0, 5, 1)) + ' (correct answer is 39.10318784326239)'
    print 'Radiation exposure between point 5 and 11: ' + str(radiationExposure(5, 11, 1)) + ' (correct answer is 22.94241041057671)'
    print 'Radiation exposure between point 0 and 11: ' + str(radiationExposure(0, 11, 1)) + ' (correct answer is 62.0455982538)'
    print 'Radiation exposure between point 40 and 100: ' + str(radiationExposure(40, 100, 1.5)) + ' (correct answer is 0.434612356115)'