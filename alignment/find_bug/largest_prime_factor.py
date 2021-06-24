def largest_prime_factor(n: int):
    """Return the largest prime factor of n.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
    Example solution:
    # line 1
    def is_prime(k):
        # line 2
        if k <= 2:
            # line 3
            return False
        # line 4
        for i in range(2, k - 1):
            # line 5
            if k % i == 0:
                # line 6
                return False
        # line 7
        return True
    # line 8
    largest = 1
    # line 9
    for j in range(2, n):
        # line 10
        if n % j == 0 and is_prime(j):
            # line 11
            largest = max(largest, j)
    # line 12
    return largest
    
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("2")
    # END OF SOLUTION

def check(candidate):

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate(10)
    out = f.getvalue().strip('\n')

    assert "2" == out
    for i in range(0, 15):
        if i != 2:
            assert str(i) != out

if __name__ == '__main__':
    check(largest_prime_factor)
