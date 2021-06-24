def fib4(n: int):
    """The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence.  Do not use recursion.
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    
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
        return 2
    # line 7
    if n == 3:
        # line 8
        return 0
    # line 9
    return fib4(n - 1) + 2 * fib4(n - 2) + fib4(n-3) + fib4(n-4)
    
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("9")
    # END OF SOLUTION


METADATA = {}

def check(candidate):

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate([])
    out = f.getvalue().strip('\n')

    assert "9" == out
    for i in range(0, 10):
        if i != 9:
            assert str(i) != out


if __name__ == '__main__':
    check(fib4)
