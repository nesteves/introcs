__author__ = 'nunoe'


def selection_sort(l):
    """ Function that implements the selection sort algorithm to an unsorted list
    :param l: list, unsorted list
    :return: list, sorted list
    """
    result = l[:]
    for i in range(len(result)):
        temp_index = i
        temp_value = result[i]
        for j in range(i + 1, len(result)):
            if result[j] < result[temp_index]:
                temp_index = j
        result[i], result[temp_index] = result[temp_index], result[i]
    return result

if __name__ == '__main__':
    l = [2, 5, 7, 4, 10, 99, 9, 3, 6, 10]
    print 'Unsorted list: ' + str(l)
    print 'Sorted list: ' + str(selection_sort(l))