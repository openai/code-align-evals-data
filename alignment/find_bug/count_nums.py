def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    
    Example solution:
    # line 1
    def digits_sum(n):
        # line 2
        neg = 1
        # line 3
        if n < 0: n, neg = -1 * n, -1
        # line 4 
        n = [-int(i) for i in str(n)]
        # line 5
        n[0] = n[0] * neg
        # line 6
        return sum(n)
    # line 7
    return len(list(filter(lambda x: x > 0, [digits_sum(i) for i in arr])))
    
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
        candidate([])
    out = f.getvalue().strip('\n')

    assert "4" == out
    for i in range(0, 10):
        if i != 4:
            assert str(i) != out

if __name__ == '__main__':
    check(count_nums)
