def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    
    Example solution:
    # line 1
    a, b = x.split("/")
    # line 2
    c, d = n.split("/")
    # line 3
    numerator = int(a) * int(c)
    # line 4
    denom = int(c) * int(d)
    # line 5
    if (numerator/denom == int(numerator/denom)):
        # line 6
        return True
    # line 7
    return False
    
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("4")
    # END OF SOLUTION

def check(candidate):

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate('', '')
    out = f.getvalue().strip('\n')

    assert "4" == out
    for i in range(0, 10):
        if i != 4:
            assert str(i) != out

if __name__ == '__main__':
    check(simplify)
