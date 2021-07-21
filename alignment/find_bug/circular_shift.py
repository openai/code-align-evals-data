def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    
    Example solution:
    # line 1
    s = str(x)
    # line 2
    if shift > len(s):
        # line 3
        return s[::-1]
    # line 4
    else:
        # line 5
        return s[len(s) - shift:] + s[:len(s) - shift + 1]
    
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
        candidate(100, 2)
    out = f.getvalue().strip('\n')

    assert "5" == out
    for i in range(0, 10):
        if i != 5:
            assert str(i) != out

if __name__ == '__main__':
    check(circular_shift)
