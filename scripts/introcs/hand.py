__author__ = 'nunoe'

import random


class Hand(object):

    def __init__(self, n):
        """ Initialize the hand
        :param n: int, size of the hand
        """
        assert type(n) == int
        self.HAND_SIZE = n
        self.VOWELS = 'aeiou'
        self.CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
        self.hand = {}
        self.deal_new_hand()

    def deal_new_hand(self):
        """ Deals a new hand and sets the instance attribute to it """
        self.hand = {}

        num_vowels = self.HAND_SIZE / 3

        for i in range(num_vowels):
            v = self.VOWELS[random.randrange(0, len(self.VOWELS))]
            self.hand[v] = self.hand.get(v, 0) + 1

        for i in range(num_vowels, self.HAND_SIZE):
            c = self.CONSONANTS[random.randrange(0, len(self.CONSONANTS))]
            self.hand[c] = self.hand.get(c, 0) + 1

    def set_dummy_hand(self, hand_string):
        """ Allows the user to build a dummy hand
        :param hand_string: str, the list of letters to build the hand with
        """
        assert len(hand_string) == self.HAND_SIZE, "Length of hand_string ({0}) must equal" \
                                                   "length of HAND_SIZE ({1})".format(len(hand_string), self.HAND_SIZE)
        self.hand = {}
        for char in hand_string:
            self.hand[char] = self.hand.get(char, 0) + 1

    def calculate_len(self):
        """ Returns the length of the hand. """
        return sum([self.hand[char] for char in self.hand])

    def __str__(self):
        """ Returns a string representation of the hand. """
        return ''.join([key * self.hand[key] for key in sorted(self.hand.keys())])

    def update(self, word):
        """ Updates the hand by removing the letters composing word, when it is legal
        :param word: str, word build from the available letters in the hand
        :return: boolean, True if the word was legal, False otherwise
        """
        w = {char: word.count(char) for char in set(word)}

        if all([self.hand.get(char, 0) >= w[char] for char in w]):
            for char in word:
                self.hand[char] -= 1
            return True
        else:
            return False

if __name__ == '__main__':

    a = {'a': 1, 'b': 2}
    print str(sum([a[i] for i in a]))
    print 'a' * 3
    print ''.join([key * a[key] for key in a.keys()])

    myHand = Hand(7)
    print myHand
    print myHand.calculate_len()

    myHand.set_dummy_hand('aazzmsp')
    print myHand
    print myHand.calculate_len()

    myHand.update('za')
    print myHand

    myHand = Hand(7)
    myHand.set_dummy_hand('aulqqik')
    myHand.update('quail') # True
    print myHand # kq

    myHand = Hand(14)
    myHand.set_dummy_hand('cccllaapppttrr')
    myHand.update('claptrap') # True
    print myHand # cclprt

    myHand = Hand(4)
    myHand.set_dummy_hand('odgz')
    myHand.update('dog') # True
    print myHand # z

    myHand = Hand(30)
    myHand.set_dummy_hand('qqqwwweeerrrtttyyyuuuiiioooppp')
    myHand.update('typewriter') # True
    print myHand # eiioooppqqqrtuuuwwyy