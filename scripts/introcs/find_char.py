__author__ = 'nunoe'


def isIn(char, aStr):
    """
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    """
    if len(aStr) > 1:
        print 'Tested string: ' + aStr + ', testing with: ' + aStr[len(aStr) / 2]
    else:
        print 'Tested string: ' + aStr

    if len(aStr) <= 1:
        return char == aStr
    elif char < aStr[len(aStr) / 2]:
        return isIn(char, aStr[0:len(aStr) / 2])
    else:
        return char == aStr[len(aStr) / 2] or isIn(char, aStr[len(aStr) / 2 + 1:])


if __name__ == '__main__':
    print 'Looking for t'
    print str(isIn('t', 'aeeklmoqqtxyz'))