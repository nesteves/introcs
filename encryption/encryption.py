__author__ = 'nunoe'


import string
import random

WORDLIST_FILENAME = 'words.txt'


def load_words():
    """ Returns a list of words read from WORDLIST_FILENAME
    :return: list, all the words read from the file
    """
    print 'Loading word list from file...'
    in_file = open(WORDLIST_FILENAME, 'r')

    word_list = in_file.read().split()
    print ' ', len(word_list), "words loaded."

    return word_list


def is_word(word_list, word):
    """ Determines whether a word is valid
    :param word_list: list of str, reference words
    :param word: str, word to test
    :return: boolean, whether word is a valid word
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in word_list


def random_word(word_list):
    """ Returns a random word from a word list
    :param word_list: list of str, list of words from which to select a word
    :return: str, a random word from the list of words supplied
    """
    return random.choice(word_list)


def random_string(word_list, n):
    """ Returns a string of n words picked from a word list
    :param word_list: list of str, list of words from which to select words
    :param n: int, number of words with which to build the string
    :return: str, a string of n words from the word list
    """
    return ' '.join([random_word(word_list) for _ in range(n)])


def random_scrambled(word_list, n):
    """ Generate a string of words subjected to a sequence random shifts
    :param word_list: list of str, the list of words to use
    :param n: int, number of random words to generate and scramble
    :return: str, a scrambled string of n random words
    """
    s = random_string(word_list, n) + ' '
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return apply_shift(s, shifts)[:-1]


def get_story_string():
    """ Returns a story in encrypted text
    :return: str, the encrypted string
    """
    return open('story.txt', 'r').read()


def build_coder(shift):
    """ Returns a dictionary that can apply a Caesar Cipher to a letter
    The cipher is defined by the shift value. Ignores non-letter characters
    :param shift: int  => 0 and < 26
    :return: dict
    """
    alphabet = string.ascii_lowercase
    cipher_lower = {char: alphabet[(alphabet.index(char) + shift) % (len(alphabet))] for char in alphabet}
    cipher_upper = {char.upper(): cipher_lower[char].upper() for char in cipher_lower}
    return dict(cipher_lower.items() + cipher_upper.items())


def apply_coder(text, coder):
    """ Applies the coder to the text
    :param text: str, text to be encrypted
    :param coder: dict, contains the mappings of character: shifted character
    :return: str, the encrypted text
    """
    def shift_char(c, coder):
        if c.lower() not in string.ascii_lowercase:
            return c
        else:
            return coder[c]
    return ''.join([shift_char(char, coder) for char in text])

def apply_shift(text, shift):
    """ Returns a Caesar shifted text by the given shift offset.
    Letters retain their case and punctuation is ignored.
    :param text: str, text on which to apply the Caesar shift
    :param shift: int >= 0 and < 26, amount to shift the text
    :return: str, text after being shifted by specified amount
    """
    return apply_coder(text, build_coder(shift))

def find_best_shift(word_list, text):
    """ Returns a shift key that can decrypt the encoded text.
    :param word_list: list, set of valid words
    :param text: str, the text to be decrypted
    :return: int >= 0 and < 26
    """


def decrypt_story():
    """ Decrypts the store given by get_story_string().
    :return: str, the decrypted story
    """


if __name__ == '__main__':
    print build_coder(3)

    word_list = load_words()

    s = apply_shift('Hello, world!', 8)
    best_shift = find_best_shift(word_list, s)
    assert apply_shift(s, best_shift) == 'Hello, world!'