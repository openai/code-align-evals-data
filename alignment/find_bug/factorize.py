from typing import List


def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    
    Example solution:
    # line 1
    import math
    # line 2
    fact = []
    # line 3
    i = 2
    # line 4
    while i <= int(math.sqrt(n) + 1):
        # line 5
        if n % i == 0:
            # line 6
            fact.append(i)
            # line 7
            n //= i
        # line 8
        else:
            # line 9
            i += 1
    # line 10
    if n > 0:
        # line 11
        fact.append(n)
    # line 12
    return fact
    
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("10")
    # END OF SOLUTION


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}

def check(candidate):

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate(10)
    out = f.getvalue().strip('\n')

    assert "10" == out
    for i in range(0, 15):
        if i != 10:
            assert str(i) != out

if __name__ == '__main__':
    check(factorize)
