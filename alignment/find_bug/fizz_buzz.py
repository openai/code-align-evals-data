def fizz_buzz(n: int):
    """This function:
    1.  Prints every number smaller than n that's divisible by 11 or 13.
    2.  Returns the number of times the digit 7 appears.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    
    Example solution:
    # line 1
    ns = []
    # line 2
    for i in range(n):
        # line 3
        if i % 11 == 0 or i % 13 == 0:
            # line 4
            ns.append(i)
    # line 5
    s = ''.join(list(map(str, ns)))
    # line 6
    ans = 0
    # line 7
    for c in s:
        # line 8
        ans += (s == '7')
    # line 9
    return ans
    
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
    check(fizz_buzz)
