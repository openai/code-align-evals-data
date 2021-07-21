def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n, k) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    32

    The function will receive an integer as input and should return the special
    factorial of this integer.
    
    Example solution:
    # line 1
    fact_i = 1
    # line 2
    special_fact = 1
    # line 3
    for i in range(1, n+1):
        # line 4
        fact_i *= i
        # line 5
        special_fact *= (fact_i - 1)
    # line 6
    return special_fact
    
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
        candidate(10)
    out = f.getvalue().strip('\n')

    assert "5" == out
    for i in range(0, 10):
        if i != 5:
            assert str(i) != out

if __name__ == '__main__':
    check(special_factorial)
