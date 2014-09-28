__author__ = 'nunoe'


def interlace(s1, s2):
    """ Returns an interlaced string comprised of the characters from s1 and s2
    :param s1: str, the first string, elements in the resulting string
    start with the first character from this string
    :param s2: str, the second string
    :return: str, an interlaced string, where elements alternate between characters from s1 and s2.
    Starts with a character from s1
    """
    if len(s2) > len(s1):
        min_length = len(s1)
        big_str = s2
    else:
        min_length = len(s2)
        big_str = s1
    return ''.join([s1[i] + s2[i] for i in range(min_length)]) + big_str[min_length:]


def interlace_recur(s1, s2):
    """ Returns an interlaced string comprised of the characters from s1 and s2 - Recursively
    :param s1: str, the first string, elements in the resulting string
    start with the first character from this string
    :param s2: str, the second string
    :return: str, an interlaced string, where elements alternate between characters from s1 and s2.
    Starts with a character from s1
    """
    def interlace_helper(s1, s2, out):
        if s1 == '':
            return out + s2
        elif s2 == '':
            return out + s1
        else:
            return interlace_helper(s1[1:], s2[1:], out + s1[0] + s2[0])
    return interlace_helper(s1, s2, '')


if __name__ == '__main__':
    print '1: ' + interlace('', '')
    print '2: ' + interlace('ace', 'bdfgh')
    print '3: ' + interlace('bdfgh', 'ace')

    print '4: ' + interlace_recur('', '')
    print '5: ' + interlace_recur('ace', 'bdfgh')
    print '6: ' + interlace_recur('bdfgh', 'ace')