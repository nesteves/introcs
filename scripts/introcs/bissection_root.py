__author__ = 'nunoe'

def bissection_root(value, power, epsilon):
    """ function used to find the root of a given value through bissection search

    :param value: int, number for which we want to find the root
    :param power: int, power that turns the root into the given value
    :param epsilon: float, tolerance used when testing the root
    :return: float, the root of the given value
    """
    lower_bound = min(0, value)
    upper_bound = max(0, value)
    result = 0.0
    while abs(result ** power - value) >= epsilon:
        if result ** power > value:
            upper_bound = result
        else:
            lower_bound = result
        result = (lower_bound + upper_bound) / 2.0

    return result


if __name__ == '__main__':
    print 'The square root of 25 is ' + str(bissection_root(25, 2, 0.001))