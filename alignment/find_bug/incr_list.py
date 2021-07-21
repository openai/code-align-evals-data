def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    
    Example solution:
    # line 1
    ret = []
    # line 2
    for x in l:
        # line 3
        ret.append(x + 1)
    # line 4
    return list(set(ret))
    
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("4")
    # END OF SOLUTION


METADATA = {}

def check(candidate):

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate([])
    out = f.getvalue().strip('\n')

    assert "4" == out
    for i in range(0, 10):
        if i != 4:
            assert str(i) != out


if __name__ == '__main__':
    check(incr_list)
