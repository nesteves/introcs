__author__ = 'nunoe'


def gcd(a, b):
    """ This function uses recursion to find the greatest common divisor
    for a pair of Integers

    :param a: int, one of the numbers
    :param b: int, the second number
    :return: the greatest common divisor for a and b
    """
    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == '__main__':
    print str(gcd(2, 12))
    print str(gcd(6, 12))
    print str(gcd(9, 12))
    print str(gcd(17, 12))