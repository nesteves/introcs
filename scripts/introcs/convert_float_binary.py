__author__ = 'nunoe'


def binary_from_float(n):
    print 'Given number: {0}'.format(n)
    p = 0
    while ((2 ** p) * n) % 1 != 0:
        print 'Remainder: ' + str((2 ** p) * n - int((2 ** p) * n))
        p += 1

    num = int(n * (2 ** p))
    print 'The resulting whole number (n * p) is: {0}'.format(num)

    result = ''
    if num == 0:
        result = '0'
    while num > 0:
        result = str(num % 2) + result
        num = num / 2

    print 'p - len(result) = ' + str(p - len(result))
    for i in range(p - len(result)):
        result = '0' + result

    print 'Result: ' + str(result)
    result = result[0:-p] + '.' + result[-p:]

    return result

if __name__ == '__main__':
    number = float(raw_input('Enter a decimal number between 0 and 1: '))
    print 'The binary representation of {0} is {1}'.format(number, binary_from_float(number))