__author__ = 'nunoe'

import unittest


class TestOddTuples(unittest.TestCase):
    """ Unit tests for the function odd_tuples
    """

    def test_empty_tuple(self):
        original_tup = ()
        self.assertEqual(odd_tuples(original_tup), original_tup)

    def test_double_value_tuple(self):
        original_tup = ('one', (1, 2, 'three'))
        self.assertEqual(odd_tuples(original_tup), ('one',))

    def test_triple_value_tuple(self):
        original_tup = (1, 'two', 3)
        self.assertEqual(odd_tuples(original_tup), (1, 3))



def odd_tuples(a_tup):
    """ Function that takes in a tuple and returns
    another one comprised of every other element in
    the given tuple

    :param a_tup: tuple
    :return: every other element in a_tup, starting at 0
    """

    if len(a_tup) == 0:
        return ()

    result_tup = (a_tup[0],)
    for i in range(1, len(a_tup)):
        if i % 2 == 0:
            result_tup += (a_tup[i],)

    return result_tup


if __name__ == '__main__':
    unittest.main()