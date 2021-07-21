def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    
    Example solution:
    # line 1
    l = sorted(l)
    # line 2
    if len(l) % 2 == 0:
        # line 3
        return l[len(l) // 2]
    # line 4
    else:
        # line 5
        return (l[len(l) // 2] + l[len(l) // 2 + 1]) / 2.0
    
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
        candidate([])
    out = f.getvalue().strip('\n')

    assert "2" == out
    for i in range(0, 10):
        if i != 2:
            assert str(i) != out

if __name__ == '__main__':
    check(median)
