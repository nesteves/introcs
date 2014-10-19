__author__ = 'nunoe'


def depth_first_search(root, validate_value):
    """ Function used to perform a depth first search on a binary tree
    :param root: root of a binary tree
    :param validate_value: function, to be used in evaluating the stopping condition
    :return: list, the path to the searched node if the condition is met, False otherwise
    """
    stack = [root]

    while len(stack) > 0:
        print 'At node: ' + str(stack[0])
        if validate_value(stack[0]):
            return trace_path(stack[0])
        else:
            temp = stack.pop(0)
            if temp.get_right_branch():
                stack.insert(0, temp.get_right_branch())
            if temp.get_left_branch():
                stack.insert(0, temp.get_left_branch())
    return False


def depth_first_search_no_loop(root, validate_value):
    """ Function used to perform a depth first search on a binary tree
        and avoids looping through already visited nodes
    :param root: root of a binary tree
    :param validate_value: function, to be used in evaluating the stopping condition
    :return: list, the path to the searched node if the condition is met, False otherwise
    """
    stack = [root]
    items_seen = []
    while len(stack) > 0:
        print 'At node: ' + str(stack[0])
        if validate_value(stack[0]):
            return trace_path(stack[0])
        else:
            temp = stack.pop(0)
            items_seen.append(temp)
            if temp.get_right_branch():
                if not temp.get_right_branch() in items_seen:
                    stack.insert(0, temp.get_right_branch())
            if temp.get_left_branch():
                if not temp.get_left_branch() in items_seen:
                    stack.insert(0, temp.get_left_branch())
    return False


def breadth_first_search(root, validate_value):
    """ Function used to perform a breadth first search on a binary tree
    :param root: root of a binary tree
    :param validate_value: function, to be used in evaluating the stopping condition
    :return: list, the path to the searched node if the condition is met, False otherwise
    """

    queue = [root]

    while len(queue) > 0:
        print 'At node: ' + str(queue[0])
        if validate_value(queue[0]):
            return trace_path(queue[0])
        else:
            temp = queue.pop(0)
            if temp.get_left_branch():
                queue.append(temp.get_left_branch())
            if temp.get_right_branch():
                queue.append(temp.get_right_branch())
    return False


def depth_first_search_ordered(root, validate_value, less_than_value):
    """ Function used to perform a depth first search on an ordered binary tree
        - values lower than the current node are stored to the left
        - values higher than the current node are stored to the right
    :param root: root of an ordered binary tree
    :param validate_value: function, to be used in evaluating the stopping condition
    :param less_than_value: function, used to compare the node values
    :return: list, the path to the searched node if the condition is met, False otherwise
    """
    stack = [root]

    while len(stack) > 0:
        print 'At node: ' + str(stack[0])
        if validate_value(stack[0]):
            return trace_path(stack[0])
        elif less_than_value(stack[0]):
            temp = stack.pop(0)
            if temp.get_left_branch():
                stack.insert(0, temp.get_left_branch())
        else:
            temp = stack.pop(0)
            if temp.get_right_branch():
                stack.insert(0, temp.get_right_branch())
    return False


def breadth_first_search_ordered(root, validate_value, less_than_value):
    """ Function used to perform a breadth first search on an ordered binary tree
        - values lower than the current node are stored to the left
        - values higher than the current node are stored to the right
    :param root: root of a binary tree
    :param validate_value: function, to be used in evaluating the stopping condition
    :param less_than_value: function, used to compare the node values
    :return: list, the path to the searched node if the condition is met, False otherwise
    """
    queue = [root]

    while len(queue) > 0:
        print 'At node: ' + str(queue[0])
        if validate_value(queue[0]):
            return trace_path(queue[0])
        elif less_than_value(queue[0]):
            temp = queue.pop(0)
            if temp.get_left_branch():
                queue.append(temp.get_left_branch())
        else:
            temp = queue.pop(0)
            if temp.get_right_branch():
                queue.append(temp.get_right_branch())
    return False


def trace_path(node):
    """ Recursive function that returns a list detailing the path to the first node
    :param node: a node from the binary tree
    :return: the parent node of the given node
    """
    if node.get_parent():
        return trace_path(node.get_parent()) + [str(node)]
    else:
        return [str(node)]