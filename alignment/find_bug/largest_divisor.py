def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    
    Example solution:
    # line 1
    for i in range(1, n):
        # line 2
        if n % i == 0:
            # line 3
            return i
    
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("1")
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
        candidate([])
    out = f.getvalue().strip('\n')

    assert "1" == out
    for i in range(0, 10):
        if i != 1:
            assert str(i) != out




if __name__ == '__main__':
    check(largest_divisor)
