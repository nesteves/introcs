__author__ = 'nunoe'


def fun_log(number, base):
    """ Returns the logarithm of base for the given number
    :param number: int
    :param base: int
    :return: the log of base for number
    """
    return log_helper(number, base, 1)


def log_helper(number, base, current_number):
    """ Recursive function that calculates the closest integer logarithm of a number for base
    :param number: int
    :param base: int
    :param current_number: current value to do the base case check
    :return: the closest integer logarithm of a number for base
    """
    if current_number * base > number:
        return 0

    return 1 + log_helper(number, base, current_number * base)


if __name__ == '__main__':
    print 'The log base 2 of 4 is: ' + str(fun_log(4, 2))
    print 'The log base 3 of 27 is: ' + str(fun_log(27, 3))
    print 'The log base 2 of 16 is: ' + str(fun_log(16, 2))
