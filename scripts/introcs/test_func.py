__author__ = 'nunoe'

# Returns the square of a given number
def square(n):
    return n * n

# Returns the type of the given number (even vs. odd)
def is_even(n):
    if n % 2 == 0:
        return 'even'
    else:
        return 'odd'


if __name__ == '__main__':
    number = int(raw_input('Please provide a number: '))

    # Perform calculations
    result1 = is_even(number)
    result2 = square(number)

    # Output the result
    print '{0} is an {1} number.'.format(number, result1)
    print 'Squaring {0} is equal to  {1}.'.format(number, result2)