def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    
    Example solution:
    # line 1
    depth = 0
    # line 2
    for b in brackets:
        # line 3
        if b == "(":
            # line 4
            depth += 1
        # line 5
        else:
            # line 6
            depth -= 1
        # line 7
        if depth < 0:
            # line 8
            return True
    # line 9
    return depth == 0
    
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("8")
    # END OF SOLUTION



METADATA = {}


def check(candidate):
    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate([])
    out = f.getvalue().strip('\n')

    assert "8" == out
    for i in range(0, 10):
        if i != 8:
            assert str(i) != out

if __name__ == '__main__':
    check(correct_bracketing)
