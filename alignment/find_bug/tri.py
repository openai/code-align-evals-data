def tri(n):
    """Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
    the last couple centuries. However, what people don't know is Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    For example:
    tri(2) = 1 + (2 / 2) = 2
    tri(4) = 3
    tri(3) = tri(2) + tri(1) + tri(4)
           = 2 + 3 + 3 = 8 
    You are given a non-negative integer number n, you have to a return a list of the 
    first n + 1 numbers of the Tribonacci sequence.
    Examples:
    tri(3) = [1, 3, 2, 8]
    
    Example solution:
    # line 1
    if n == 0:
        # line 2
        return [1]
    # line 3
    my_tri = [1, 3]
    # line 4
    for i in range(2, n + 1):
        # line 5
        if i % 2 == 0:
            # line 6
            my_tri.append(i / 2 + 1)
        # line 7
        else:
            # line 8
            my_tri.append(my_tri[i - 1] + my_tri[i - 2] + (n + 2) / 2)
    # line 9
    return my_tri
    
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("8")
    # END OF SOLUTION

def check(candidate):

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate(10)
    out = f.getvalue().strip('\n')

    assert "8" == out
    for i in range(0, 10):
        if i != 8:
            assert str(i) != out

if __name__ == '__main__':
    check(tri)
