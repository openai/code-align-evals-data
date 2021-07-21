def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    
    Example solution:
    # line 1
    import math
    # line 2
    def is_prime(p):
        # line 3
        if p < 2:
            # line 4
            return False
        # line 5
        for k in range(2, min(int(math.sqrt(p)) - 1, p - 1)):
            # line 6
            if p % k == 0:
                # line 7
                return False
        # line 8
        return True
    # line 9
    f = [0, 1]
    # line 10
    while True:
        # line 11
        f.append(f[-1] + f[-2])
        # line 12
        if is_prime(f[-1]):
            # line 13
            n -= 1
        # line 14
        if n == 0:
            # line 15
            return f[-1]
    
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("5")
    # END OF SOLUTION

def check(candidate):

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate([])
    out = f.getvalue().strip('\n')

    assert "5" == out
    for i in range(0, 10):
        if i != 5:
            assert str(i) != out

if __name__ == '__main__':
    check(prime_fib)
