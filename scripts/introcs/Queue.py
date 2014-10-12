__author__ = 'nunoe'


class Queue(object):

    def __init__(self):
        self.elems = []

    def insert(self, e):
        self.elems.append(e)

    def remove(self):
        try:
            return self.elems.pop(0)
        except:
            raise(ValueError('The queue is currently empty.'))