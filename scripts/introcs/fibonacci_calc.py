__author__ = 'nunoe'

def fibonacci_comp(n):
    """ Returns the nth Fibonacci series term

    :param n: int, the value for which the Fibonacci series term is to be computed
    :return: int, the nth term in the Fibonacci series
    """
    if n == 1 or n == 0:
        return 1
    return fibonacci_comp(n - 1) + fibonacci_comp(n - 2)

if __name__ == '__main__':
    print '3rd term of the Fibonacci series: ' + str(fibonacci_comp(3))
    print '5th term of the Fibonacci series: ' + str(fibonacci_comp(5))