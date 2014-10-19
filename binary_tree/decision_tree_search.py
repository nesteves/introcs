__author__ = 'nunoe'

from binary_tree import *


def build_decision_tree(so_far, remaining):
    """ Builds a binary decision tree recursively and returns its root
    :param so_far: list, represents the currently selected items in the node
    :param remaining: list, represents them items which will or won't be included in the following nodes
    :return: the root node of the binary decision tree

    NOTE: Building the tree should be done at the same time the search is performed
    """

    if len(remaining) == 0:
        return Binary_Tree(so_far)
    else:
        include_element = build_decision_tree(so_far + [remaining[0]], remaining[1:])
        without_element = build_decision_tree(so_far, remaining[1:])
        current_node = Binary_Tree(so_far)
        current_node.set_left_branch(include_element)
        current_node.set_right_branch(without_element)
        return current_node


def depth_first_search_dtree(root, value_function, constraint_function):
    """ Function used to perform a depth first search on a binary decision tree
    :param root: root of a binary decision tree
    :param value_function: function, returns the value for the next item to add
    :param constraint_function:  function, validates whether there is enough room for the next item
    :return: list, the set of items that give the maximum value subject to the existing constraints
    """
    stack = [root]
    solution = None
    nodes_visited = 0

    while len(stack) > 0:
        nodes_visited += 1
        if constraint_function(stack[0].get_value()):
            if solution is None:
                solution = stack[0]
            elif value_function(stack[0].get_value()) > value_function(solution.get_value()):
                solution = stack[0]
            temp = stack.pop(0)
            if temp.get_right_branch():
                stack.insert(0, temp.get_right_branch())
            if temp.get_left_branch():
                stack.insert(0, temp.get_left_branch())
        else:
            stack.pop(0)

    print "Visited {} nodes".format(nodes_visited)
    return solution


def breadth_first_search_dtree(root, value_function, constraint_function):
    """ Function used to perform a breadth first search on a binary decision tree
    :param root: root of a binary decision tree
    :param value_function: function, returns the value for the next item to add
    :param constraint_function:  function, validates whether there is enough room for the next item
    :return: list, the set of items that give the maximum value subject to the existing constraints
    """
    queue = [root]
    solution = None
    nodes_visited = 0

    while len(queue) > 0:
        nodes_visited += 1
        if constraint_function(queue[0].get_value()):
            if solution is None:
                solution = queue[0]
            elif value_function(queue[0].get_value()) > value_function(solution.get_value()):
                solution = queue[0]
            temp = queue.pop(0)
            if temp.get_left_branch():
                queue.append(temp.get_left_branch())
            if temp.get_right_branch():
                queue.append(temp.get_right_branch())
        else:
            queue.pop(0)

    print "Visited {} nodes".format(nodes_visited)
    return solution


def depth_first_search_dtree_approx(root, value_function, constraint_function, approx_function):
    """ Function used to perform a depth first search on a binary decision tree, stopping when a sufficiently good value is found
    :param root: root of a binary decision tree
    :param value_function: function, returns the value for the next item to add
    :param constraint_function:  function, validates whether there is enough room for the next item
    :param approx_function: function, validates if the solution is sufficient
    :return: list, the set of items that give the maximum value subject to the existing constraints
    """
    stack = [root]
    solution = None
    nodes_visited = 0

    while len(stack) > 0:
        nodes_visited += 1
        if constraint_function(stack[0].get_value()):
            if solution is None:
                solution = stack[0]
            elif value_function(stack[0].get_value()) > value_function(solution.get_value()):
                solution = stack[0]
            if approx_function(solution.get_value()):
                print "Visited {} nodes".format(nodes_visited)
                return solution
            temp = stack.pop(0)
            if temp.get_right_branch():
                stack.insert(0, temp.get_right_branch())
            if temp.get_left_branch():
                stack.insert(0, temp.get_left_branch())
        else:
            stack.pop(0)

    print "Visited {} nodes".format(nodes_visited)
    return solution


def breadth_first_search_dtree_approx(root, value_function, constraint_function, approx_function):
    """ Function used to perform a breadth first search on a binary decision tree, stopping when a sufficiently good value is found
    :param root: root of a binary decision tree
    :param value_function: function, returns the value for the next item to add
    :param constraint_function:  function, validates whether there is enough room for the next item
    :param approx_function: function, validates if the solution is sufficient
    :return: list, the set of items that give the maximum value subject to the existing constraints
    """
    queue = [root]
    solution = None
    nodes_visited = 0

    while len(queue) > 0:
        nodes_visited += 1
        if constraint_function(queue[0].get_value()):
            if solution is None:
                solution = queue[0]
            elif value_function(queue[0].get_value()) > value_function(solution.get_value()):
                solution = queue[0]
            if approx_function(solution.get_value()):
                print "Visited {} nodes".format(nodes_visited)
                return solution
            temp = queue.pop(0)
            if temp.get_left_branch():
                queue.append(temp.get_left_branch())
            if temp.get_right_branch():
                queue.append(temp.get_right_branch())
        else:
            queue.pop(0)

    print "Visited {} nodes".format(nodes_visited)
    return solution


def decision_tree_implicit(to_consider, available):
    """ Recursive function that searches through an implicit decision binary tree
    :param to_consider: list of lists, the set of items with values and weights
    :param available: number, remaining weight to be taken by items
    :return: value of the solution and the solution itself
    """
    if to_consider == [] or available == 0:
        result = (0, ())
    elif to_consider[0][1] > available:
        result = decision_tree_implicit(to_consider[1:], available)
    else:
        next_item = to_consider[0]
        with_next_value, with_next_solution = decision_tree_implicit(to_consider[1:], available - next_item[1])
        with_next_value += next_item[0]
        without_next_value, without_next_solution = decision_tree_implicit(to_consider[1:], available)
        if with_next_value > without_next_value:
            result = (with_next_value, with_next_solution + (next_item,))
        else:
            result = (without_next_value, without_next_solution)
    return result
