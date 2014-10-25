__author__ = 'nunoe'

class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name


def insert(atMe, newFrob):
    if atMe.myName() < newFrob.myName():
        if atMe.getAfter() is not None:
            insert(atMe.getAfter(), newFrob)
        else:
            atMe.setAfter(newFrob)
            newFrob.setBefore(atMe)
    else:
        if atMe.getBefore() is None:
            atMe.setBefore(newFrob)
            newFrob.setAfter(atMe)
        elif atMe.getBefore().myName() <= newFrob.myName():
            newFrob.setBefore(atMe.getBefore())
            newFrob.getBefore().setAfter(newFrob)
            atMe.setBefore(newFrob)
            newFrob.setAfter(atMe)
        else:
            insert(atMe.getBefore(), newFrob)


def print_list(item):
    while item.getBefore() is not None:
        item = item.getBefore()
    while item is not None:
        print item.myName()
        item = item.getAfter()


def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list
    """
    if start.getBefore() is None:
        return start
    else:
        return findFront(start.getBefore())


test_list = Frob('leonid')
a = Frob('amara')
j1 = Frob('jennifer')
j2 = Frob('jennifer')
s = Frob('scott')

print '1'
print_list(test_list)
insert(test_list, s)
print '2'
print_list(test_list)
insert(s, j1)
print '3'
print_list(test_list)
insert(s, j2)
print '4'
print_list(test_list)
insert(j1, a)
print '5'
print_list(test_list)

print
print 'Find Front'
print findFront(a).myName()
print findFront(j1).myName()
print findFront(j2).myName()
print findFront(s).myName()
