def fibfib(n: int):
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    
    Example solution:
    # line 1
    if n == 0:
        # line 2
        return 0
    # line 3
    if n == 1:
        # line 4
        return 0
    # line 5
    if n == 2:
        # line 6
        return 1
    # line 7
    return fibfib(n - 1) + fibfib(n - 2) + 3 * fibfib(n - 3)
    
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("7")
    # END OF SOLUTION


METADATA = {}

def check(candidate):

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate([])
    out = f.getvalue().strip('\n')

    assert "7" == out
    for i in range(0, 10):
        if i != 7:
            assert str(i) != out


if __name__ == '__main__':
    check(fibfib)
