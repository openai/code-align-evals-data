def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
    Example solution:
    # line 1
    max_sum = 0
    # line 2
    s = 0
    # line 3
    for num in nums:
        # line 4
        s += num
        # line 5
        if (s < 0):
            # line 6
            s = 0
        # line 7
        max_sum = max(s, max_sum)
    # line 8
    if max_sum == 0:
        # line 9
        max_sum = max(-i for i in nums)
    # line 10
    min_sum = -max_sum
    # line 11
    return min_sum
    
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
    for i in range(0, 15):
        if i != 4:
            assert str(i) != out

if __name__ == '__main__':
    check(minSubArraySum)
