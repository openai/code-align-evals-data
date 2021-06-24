def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    
    Example solution:
    # line 1
    from math import floor, ceil
    # line 2
    if value.count('.') == 1:
        # remove trailing zeros
        # line 3
        while (value[-1] == '0'):
            # line 4
            value = value[:-1]
    # line 5
    num = float(value)
    # line 6
    if value[-2:] == '.5':
        # line 7
        if num < 0:
            # line 8
            res = ceil(num)
        # line 9
        else:
            # line 10
            res = floor(num)
    # line 11
    elif len(value) > 0:
        # line 12
        res = int(round(num))
    # lien 13
    else:
        # line 14
        res = 0
    # line 15
    return res
    
    '''
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("7")
    # END OF SOLUTION

def check(candidate):

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate("")
    out = f.getvalue().strip('\n')

    assert "7" == out
    for i in range(0, 20):
        if i != 7:
            assert str(i) != out

if __name__ == '__main__':
    check(closest_integer)
