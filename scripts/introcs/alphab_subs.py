__author__ = 'nunoe'

# Finds the biggest substring written in alphabetical order
def big_alpha(s):
    curr_str = ''

    for i in range(len(s) - 1):
        curr_index = i + 1
        while curr_index < len(s) and s[curr_index] >= s[curr_index - 1]:
            curr_index += 1
        if len(s[i:curr_index]) > len(curr_str):
            print 'new proposal: {0} has a length of {1}.'.format(s[i:curr_index], len(s[curr_index]))
            print 'incumbent solution: {0} has a length of {1}.'.format(curr_str, len(curr_str))
            curr_str = s[i:curr_index]

    return curr_str


if __name__ == '__main__':
    s = 'ohcrfgffsquzx'
    print 'Longest substring in alphabetical order is: {0}'.format(big_alpha(s))
