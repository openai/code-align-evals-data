def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    
    Example solution:
    # line 1
    ret = []
    # line 2
    for i in range(1,n):
        # line 3
        if i%2 == 0:
            # line 4
            x = 1
            # line 5
            for j in range(1,i+1): x *= j
            # line 6
            ret += [x]
        # line 7
        else:
            # line 8
            x = 0
            # line 9
            for j in range(1,i+1): x += j
            # line 10
            ret += [x]
    # line 11
    return ret
    
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("2")
    # END OF SOLUTION

def check(candidate):

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate(10)
    out = f.getvalue().strip('\n')

    assert "2" == out
    for i in range(0, 15):
        if i != 2:
            assert str(i) != out

if __name__ == '__main__':
    check(f)
