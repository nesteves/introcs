__author__ = 'nunoe'


def gen_fibonacci():
    fib1 = 0
    fib2 = 1

    yield 0
    yield 1

    while True:
        next = fib1 + fib2
        yield next
        fib1 = fib2
        fib2 = next

def gen_listitems(li):
    for item in li:
        yield item


if __name__ == '__main__':
    fib = gen_fibonacci()
    print [fib.next() for i in range(20)]

    a = [i for i in range(20)]

    for i in gen_listitems(a):
        b = i
        i = 11
        print b, i

    print a