__author__ = 'nunoe'

def is_palindrome(s):
    """ Tests a string to find out if it is or not a palindrome

    :param s: str, given String to be tested
    :return: True if s is a palindrome, false if it is not
    """

    def to_char(s):
        """ Converts a given string into a list of lower case characters

        :param s: str, given String to be converted
        :return:
        """
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans += c
        return ans

    def is_pal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_pal(s[1:-1])

    return is_pal(to_char(s))

if __name__ == '__main__':
    print 'Is ablewasiereisawelba a palindrome? ' + str(is_palindrome('ablewasiereisawelba'))
    print 'Is derp a palindrome? ' + str(is_palindrome('derp'))