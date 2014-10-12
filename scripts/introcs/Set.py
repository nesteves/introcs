__author__ = 'nunoe'


class IntSet(object):
    """ An IntSet is a set of Integers
    The data is represented by a list of integers, self.vals
    Each int in the set occurs in self.vals exactly once """

    def __init__(self):
        """
        Creates the empty list of integers
        """
        self.vals = []

    def insert(self, e):
        """ Inserts e into self.vals if it doesn't already occur in the list
        :param e: int, value to be inserted into self.vals
        :return: nothing
        """
        if e not in self.vals:
            self.vals.append(e)

    def member(self, e):
        """ Tests whether a value occurs in self.vals
        :param e: int, value to be searched for in self.vals
        :return: boolean, True if the e is in self.vals, False otherwise
        """
        return e in self.vals

    def remove(self, e):
        """ Removes a value from the set
        :param e: int, value to be removed from the self.vals
        :return: nothing, throws an error if the value does not exist in the set
        """
        try:
            self.vals.remove(e)
        except:
            raise(ValueError(str(e) + ' not found.'))

    def __len__(self):
        """
        :return: int, the length of the set
        """
        return len(self.vals)

    def __str__(self):
        """
        :return: str, a sorted representation of the set
        """
        self.vals.sort()
        return '(' + ','.join([str(e) for e in self.vals]) + ')'

    def intersect(self, other):
        """ Computes the intersection between 2 IntSets
        :param other: IntSet, the set with which self.vals is to compute the intersection
        :return: IntSet, a new instance representing the intersection of both sets
        """
        result = IntSet()
        map(result.insert, [e for e in self.vals if e in other.vals])
        return result


if __name__ == '__main__':
    mySet = IntSet()
    mySet.insert(4)
    mySet.insert(3)
    mySet.insert(9)
    mySet.insert(9)
    mySet.insert(7)
    mySet.insert(5)
    mySet.insert(8)
    mySet.remove(5)
    print 'The final set: ' + str(mySet)
    print 'Is the number 9 in the set: ' + str(mySet.member(9))
    print 'Is the number 5 in the set: ' + str(mySet.member(5))
    # mySet.remove(5) # Will raise a ValueError exception