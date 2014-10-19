__author__ = 'nunoe'


class Binary_Tree(object):
    """ Class used to represent binary_Trees
    """

    def __init__(self, value):
        """ Initializes the binary tree
        :param value: value to assign to the current node
        """
        self.value = value
        self.parent = None
        self.left_branch = None
        self.right_branch = None

    def set_parent(self, value):
        self.parent = value

    def set_left_branch(self, value):
        self.left_branch = value

    def set_right_branch(self, value):
        self.right_branch = value

    def get_value(self):
        return self.value

    def get_parent(self):
        return self.parent

    def get_left_branch(self):
        return self.left_branch

    def get_right_branch(self):
        return self.right_branch

    def __str__(self):
        return str(self.value)