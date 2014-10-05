__author__ = 'nunoe'

import operator


def merge_sort(l, compare = operator.lt):
    """ Recursive function that implements the merge sort algorithm to an unsorted list
    :param l: list, unsorted lists
    :param compare: function, the function used to compare two objects, should take 2 arguments
    :return: list, sorted result
    """
    if len(l) < 2:
        return l[:]
    else:
        middle = len(l) / 2
        left = merge_sort(l[:middle], compare)
        right = merge_sort(l[middle:], compare)
        return merge(left, right, compare)


def merge(left, right, compare):
    """ Function used to merge 2 lists into a single sorted list
    :param left: list, left list
    :param right: list, right list
    :param compare: function, used to compare elements from the left list with elements from the right list
    :return: a single list where all elements are sorted
    """
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


if __name__ == '__main__':
    l = [2, 5, 7, 4, 10, 99, 9, 3, 6, 10]
    print 'Unsorted list: ' + str(l)
    print 'Sorted list: ' + str(merge_sort(l))