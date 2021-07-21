def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    
    Example solution:
    # line 1
    def digits_sum(n):
        # line 2
        neg = -1
        # line 3
        if n < 0: n, neg = -1 * n, -1
        # line 4 
        n = [int(i) for i in str(n)]
        # line 5
        n[0] = n[0] * neg
        # line 6
        return sum(n)
    # line 7
    return sorted(nums, key=digits_sum)
    
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
        candidate([])
    out = f.getvalue().strip('\n')

    assert "2" == out
    for i in range(0, 10):
        if i != 2:
            assert str(i) != out

if __name__ == '__main__':
    check(order_by_points)
