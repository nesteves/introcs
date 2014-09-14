__author__ = 'nunoe'


def semordnilapWrapper(str1, str2):
    """ Wrapper function for the semordnilap function.
    Performs basic checks on the function parameters

    :param str1: a string
    :param str2: a string
    :return: a call to the recursive function semordnilap
    """
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    return semordnilap(str1, str2)


def semordnilap(str1, str2):
    """ Compare 2 strings recursively to verify if they are semordnilaps of each other

    :param str1: a string
    :param str2: a string
    :return: True if str1 and str2 are semordnilap;
             False otherwise.
    """
    if len(str1) == 0:
        return True
    else:
        return str1[0] == str2[-1] and str1[-1] == str2[0] and semordnilap(str1[1:-1], str2[1:-1])


if __name__ == '__main__':
    print 'Test 1, True expected: ' + str(semordnilapWrapper('live', 'evil'))
    print 'Test 2, False expected: ' + str(semordnilapWrapper('tact', 'cat'))
    print 'Test 3, False expected: ' + str(semordnilapWrapper('semordnilap', 'palindrome'))