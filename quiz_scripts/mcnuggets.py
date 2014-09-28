__author__ = 'nunoe'

def mcnuggets(n):
    """
    :param n: positive int, number of mcnuggets to buy
    :return: boolean, whether it is possible to find a
    combination of integers for the existing pack sizes
    to purchase the desired number o mcnuggets
    """
    a = 6
    b = 9
    c = 20

    for i in range(n / 6):
        for j in range(n / 6):
            for k in range(n / 6):
                if i + j + j > 0 and n % (a * i + b * j + c * k) == 0:
                    return True
    return False


if __name__ == '__main__':
    print '15 McNuggets: ' + str(mcnuggets(15))
    print '16 McNuggets: ' + str(mcnuggets(16))
    print '20 McNuggets: ' + str(mcnuggets(20))
    print '39 McNuggets: ' + str(mcnuggets(39))