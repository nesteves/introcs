__author__ = 'nunoe'


def print_move(fr, to):
    """ Prints the move in the game Towers of Hanoi

    :param fr: origin location
    :param to: destination location
    :return: has no return values, just prints the move
    """
    print 'Move one piece from the ' + str(fr) + ' to the ' + str(to) + '.'


def solve_towers_of_hanoi(n, fr, to, spare):
    """ Solves the game Towers of Hanoi recursively

    :param n: int, the number of pieces on the current stack
    :param fr: place where the current stack is
    :param to: place to where the current stack is to be moved to
    :param spare: spare location that can be used during the game
    :return: has no return values, just prints every move sequentially using the print_move function
    """
    if n == 1:
        print_move(fr, to)
    else:
        solve_towers_of_hanoi(n - 1, fr, spare, to)
        solve_towers_of_hanoi(1, fr, to, spare)
        solve_towers_of_hanoi(n - 1, spare, to, fr)

if __name__ == '__main__':
    solve_towers_of_hanoi(5, 'origin', 'destination', 'spare point')