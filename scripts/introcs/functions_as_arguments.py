__author__ = 'nunoe'


def apply_to_each(f, L):
    """ This function applies a given function to every element of
        a list
    :param f: function, to be applied to each element of L
    :param L: list, to be iterated over
    :return:
    """
    newL = L[:]
    for i in range(len(L)):
        newL[i] = f(newL[i])
    return newL


def apply_funs_to(F, n):
    """ This function applies a given list of functions
        to a given number
    :param F: list of functions, to be applied to the given value
    :param n: num
    :return: the list of results of applying the function to the number
    """
    result_list = []
    for i in range(len(F)):
        result_list.append(F[i](n))
    return result_list


def increase_by_3(n):
    return n + 3


def multipy_by_2(n):
    return n * 2


def divide_by_2(n):
    return n / 2


def is_even(n):
    return n % 2 == 0


if __name__ == '__main__':
    # Apply single function to a list of values
    a_list = range(10)
    apply_to_each(increase_by_3, a_list)
    print apply_to_each(increase_by_3, a_list)

    # Apply a list of functions to a single value
    list_of_funs = [increase_by_3, multipy_by_2, divide_by_2, is_even]
    print apply_funs_to(list_of_funs, 4)