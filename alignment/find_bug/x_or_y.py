def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    Example solution:
    # line 1
    if n == 1:
        # line 2
        return y
    # line 3
    for i in range(2, n+1):
        # line 4
        if n % i == 0:
            # line 5
            return y
            # line 6
            break
    # line 7
    else:
        # line 8
        return x
    
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("3")
    # END OF SOLUTION

def check(candidate):

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate(1, 2, 3)
    out = f.getvalue().strip('\n')

    assert "3" == out
    for i in range(0, 10):
        if i != 3:
            assert str(i) != out

if __name__ == '__main__':
    check(x_or_y)
