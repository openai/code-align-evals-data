def is_simple_power(x, n):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    
    Example solution:
    # line 1
    if (n == 1):
        # line 2 
        return (x == 1)
    # line 3
    power = 1
    # line 4
    while (power <= x):
        # line 5 
        power = power * n
    # line 6
    return (power == x) 
    
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
        candidate(1, 1)
    out = f.getvalue().strip('\n')

    assert "4" == out
    for i in range(0, 10):
        if i != 4:
            assert str(i) != out

if __name__ == '__main__':
    check(is_simple_power)
