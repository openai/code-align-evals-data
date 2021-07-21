def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    
    Example solution:
    # line 1
    lower = max(2, min(a, b))
    # line 2
    upper = min(8, max(a, b))
    # line 3
    return [i for i in range(lower, upper) if i % 2 == 0]
    
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("3")
    # END OF SOLUTION

def check(candidate):

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate(1, 2)
    out = f.getvalue().strip('\n')

    assert "3" == out
    for i in range(0, 10):
        if i != 3:
            assert str(i) != out
            
if __name__ == '__main__':
    check(generate_integers)
