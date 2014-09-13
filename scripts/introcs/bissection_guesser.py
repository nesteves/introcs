__author__ = 'nunoe'


def guess_number(lower_bound, upper_bound):
    print 'Please think of a number between ' + str(lower_bound) + ' and ' + str(upper_bound) + '!'
    current_guess = 0
    answer = ''
    while answer != 'c':
        current_guess = (lower_bound + upper_bound) / 2
        print 'Is your secret number ' + str(current_guess) + '?'
        answer = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l'"
                           " to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
        if answer == 'h':
            upper_bound = current_guess
        elif answer == 'l':
            lower_bound = current_guess
        elif answer != 'c':
            print 'Sorry, I did not understand your input.'

    return current_guess

if __name__ == '__main__':
    result = guess_number(0, 100)
    print 'Game over. Your secret number was ' + str(result)