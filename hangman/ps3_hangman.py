__author__ = 'nunoe'

import random
import string

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """ Function used to obtain the list of valid words from words.txt
    :return: list, valid words - strings of lowercase
        letters
    """
    print 'Loading word list from file...'
    f = open(WORDLIST_FILENAME, 'r', 0)
    line = f.readline()

    wordlist = string.split(line)
    print ' ', len(wordlist), 'words loaded.'
    return wordlist


def chooseWord(wordlist):
    """  Returns a word chosen at random from a give list of words
    :param wordlist: list, the set of words to choose from
    :return: str, word selected at random from wordlist
    """
    return random.choice(wordlist)


def isWordGuessed(secretWord, lettersGuessed):
    """
    :param secretWord: str, the word that the user has to guess
    :param lettersGuessed: list, the letters guessed so far
    :return: boolean, True if all the letters of secretWord are in lettersGuessed
        False otherwise
    """
    return all([letter in lettersGuessed for letter in list(secretWord)])

def getGuessedWord(secretWord, lettersGuessed):
    """ Returns letters and empty spaces representing the part of the word guessed so far
    :param secretWord: str, the word that the user has to guess
    :param lettersGuessed: list, the letters guessed so far
    :return: str, letters and underscores that represent the current state of
        the game
    """
    def letter_or_space(letter, guesses):
        if letter in guesses:
            return letter
        else:
            return '_'

    return ''.join([letter_or_space(letter, lettersGuessed) for letter in secretWord])


def getAvailableLetters(lettersGuessed):
    """ Returns the string of words that have not been guessed so far
    :param lettersGuessed: list, letters that have been guessed so far
    :return: str, all the letters that have not yet been guessed
    """
    alphabet = string.ascii_lowercase
    return ''.join([i for i in alphabet if i not in lettersGuessed])


def hangman(secretWord):
    """ Starts up an interactive game of Hangman
        * At the start of the game lets the user know how many
            letters the secretWord contains;
        * Asks the user to supply one guess (letter) per round
            The user has a total of 8 guesses (spent when it is
            incorrect)
        * The user receives feedback after each guess, as well
            as the partially guessed word so far (underscores
            represent the not yet guessed letters)

    :param secretWord: str, the secret word to guess
    :return: None
    """
    guesses_left = 8
    letters_guessed = []
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.'
    print '_____________'

    while guesses_left > 0:
        print 'You have ' + str(guesses_left) + ' guesses left.'
        print 'Available letters: ' + str(getAvailableLetters(letters_guessed))
        guess = raw_input('Please guess a letter: ').lower()

        if guess not in letters_guessed:
            letters_guessed.append(guess)
            if guess in secretWord:
                print 'Good guess: ' + str(getGuessedWord(secretWord, letters_guessed))
            else:
                guesses_left -= 1
                print 'Oops! That letter is not in my word: ' + str(getGuessedWord(secretWord, letters_guessed))
        else:
            print 'Oops! You\'ve already guessed that letter: ' + str(getGuessedWord(secretWord, letters_guessed))

        print '_____________'

        if isWordGuessed(secretWord, letters_guessed):
            print 'Congratulations, you won!'
            break

    if guesses_left == 0:
        print 'Sorry, you ran out of guesses. The word was ' + secretWord





if __name__ == '__main__':
    wordlist = loadWords()
    secretWord = chooseWord(wordlist).lower()
    hangman('derp')