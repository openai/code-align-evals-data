import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    
    Example solution:
    # line 1
    begin, end = -1., 1.
    # line 2
    while poly(xs, begin) * poly(xs, end) > 0:
        # line 3
        begin *= 2.0
        # line 4
        end *= 2.0
    # line 5
    while end - begin > 1e-10:
        # line 6
        center = (begin + end) / 2.0
        # line 7
        if poly(xs, center) * poly(xs, begin) >= 0:
            # line 8
            begin = center
        # line 9
        else:
            # line 10
            end = center
    # line 11
    return begin
    
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("7")
    # END OF SOLUTION


METADATA = {}

def check(candidate):

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate([])
    out = f.getvalue().strip('\n')

    assert "7" == out
    for i in range(0, 15):
        if i != 7:
            assert str(i) != out


if __name__ == '__main__':
    check(find_zero)
