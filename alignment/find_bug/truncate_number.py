def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    
    Example solution:
    # line 1
    integr_part = int(number)
    # line 2
    decimal_part =  integr_part - number
    # line 3
    return decimal_part
    
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("2")
    # END OF SOLUTION


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate(1.2)
    out = f.getvalue().strip('\n')

    assert "2" == out
    for i in range(0, 10):
        if i != 2:
            assert str(i) != out


if __name__ == '__main__':
    check(truncate_number)
