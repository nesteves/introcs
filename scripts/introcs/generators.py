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


def genPrimes():
    yield 2
    yield 3
    primes = [2, 3]
    n = 3
    while True:
        n += 1
        is_prime = True
        for i in primes:
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
            yield n


def gen_listitems(li):
    for item in li:
        yield item


if __name__ == '__main__':

    # Fibonacci generator
    fib = gen_fibonacci()
    print [fib.next() for i in range(20)]

    # Prime number generator
    pri = gen_primes()
    print [pri.next() for i in range(20)]

    a = [i for i in range(20)]
    b = []
    for i in gen_listitems(a):
        # Changing i does not effect the original list a
        i = 11
        b.append(i)

    print a
    print b