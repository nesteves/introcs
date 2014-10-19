__author__ = 'nunoe'

from binary_tree import *
from tree_search import *
from decision_tree_search import *


def find6(node):
    return node.get_value() == 6


def less_than6(node):
    return node.get_value() > 6


def find5(node):
    return node.get_value() == 5


def less_than5(node):
    return node.get_value() > 5


def find9(node):
    return node.get_value() == 9


def less_than9(node):
    return node.get_value() > 9


def sum_values(lst):
    vals = [e[0] for e in lst]
    return sum(vals)


def sum_weights(lst):
    wts = [e[1] for e in lst]
    return sum(wts)


def weight_below_10(lst):
    return sum_weights(lst) <= 10


def weight_below_6(lst):
    return sum_weights(lst) <= 6


def at_least_15(lst):
    return sum_values(lst) >= 15


if __name__ == '__main__':

    """ Test binary trees and search algorithms for this data structure
    The tree created here has the following structure:
                5
              /   \
            2      8
           / \    /
          1   4  6
             /    \
            3      7
    """

    n5 = Binary_Tree(5)
    n2 = Binary_Tree(2)
    n1 = Binary_Tree(1)
    n4 = Binary_Tree(4)
    n8 = Binary_Tree(8)
    n6 = Binary_Tree(6)
    n7 = Binary_Tree(7)
    n3 = Binary_Tree(3)

    n5.set_left_branch(n2)
    n2.set_parent(n5)
    n5.set_right_branch(n8)
    n8.set_parent(n5)
    n2.set_left_branch(n1)
    n1.set_parent(n2)
    n2.set_right_branch(n4)
    n4.set_parent(n2)
    n8.set_left_branch(n6)
    n6.set_parent(n8)
    n6.set_right_branch(n7)
    n7.set_parent(n6)
    n4.set_left_branch(n3)
    n3.set_parent(n4)

    # Test depth first search
    print 'Testing depth first search'
    print 'Was the value 6 found? ' + str(depth_first_search(n5, find6))
    print 'Was the value 5 found? ' + str(depth_first_search(n5, find5))
    print 'Was the value 9 found? ' + str(depth_first_search(n5, find9))
    print ''

    # Test breadth first search
    print 'Testing breadth first search'
    print 'Was the value 6 found? ' + str(breadth_first_search(n5, find6))
    print 'Was the value 5 found? ' + str(breadth_first_search(n5, find5))
    print 'Was the value 9 found? ' + str(breadth_first_search(n5, find9))
    print ''

    # Test depth first ordered search
    print 'Testing depth first ordered search'
    print 'Was the value 6 found? ' + str(depth_first_search_ordered(n5, find6, less_than6))
    print 'Was the value 5 found? ' + str(depth_first_search_ordered(n5, find5, less_than5))
    print 'Was the value 9 found? ' + str(depth_first_search_ordered(n5, find9, less_than9))
    print ''

    # Test breadth first ordered search
    print 'Testing breadth first ordered search'
    print 'Was the value 6 found? ' + str(breadth_first_search_ordered(n5, find6, less_than6))
    print 'Was the value 5 found? ' + str(breadth_first_search_ordered(n5, find5, less_than5))
    print 'Was the value 9 found? ' + str(breadth_first_search_ordered(n5, find9, less_than9))
    print ''

    # Searching binary decision trees
    a = [6, 3]
    b = [7, 2]
    c = [8, 4]
    d = [9, 5]

    decision_tree_test = build_decision_tree([], [a, b, c, d])

    # Test depth first search on binary decision trees
    print 'Test depth first search on binary decision trees'
    print 'The best solution for a maximum weight of 10? ' + \
          str(depth_first_search_dtree(decision_tree_test, sum_values, weight_below_10))
    print 'The best solution for a maximum weight of 6? ' + \
          str(depth_first_search_dtree(decision_tree_test, sum_values, weight_below_6))
    print ''

    # Test breadth first search on binary decision trees
    print 'Test breadth first search on binary decision trees'
    print 'The best solution for a maximum weight of 10? ' + \
          str(breadth_first_search_dtree(decision_tree_test, sum_values, weight_below_10))
    print 'The best solution for a maximum weight of 6? ' + \
          str(breadth_first_search_dtree(decision_tree_test, sum_values, weight_below_6))
    print ''

    # Test both searches with stopping criteria
    print 'Test both searches with stopping criteria'
    print 'The best solution for a maximum weight of 10? ' + \
          str(depth_first_search_dtree_approx(decision_tree_test, sum_values, weight_below_10, at_least_15))
    print 'The best solution for a maximum weight of 6? ' + \
          str(breadth_first_search_dtree_approx(decision_tree_test, sum_values, weight_below_10, at_least_15))
    print ''

    # Test depth search on implicit binary decision trees
    print 'Test depth search on implicit binary decision trees'
    items = [a, b, c, d]
    value, solution = decision_tree_implicit(items, 10)
    print 'For an available weight of 10, the best solution is: ' + str(solution)
    print 'With a global value of: ' + str(value)