def intersection(interval1, interval2):
    """You are given two intervals of integers,
    each interval is a pair of integers. For example, interval = (start, end) = (1, 2).
    The given intervals are closed which means that the interval (start, end)
    includes both start and end.
    For each given interval, it is assumed that its start is less or equal its end.
    Your task is to determine whether the length of intersection of these two 
    intervals is a prime number.
    Example, the intersection of the intervals (1, 3), (2, 4) is (2, 3)
    which its length is 1, which not a prime number.
    If the length of the intersection is a prime number, return "YES",
    otherwise, return "NO".
    If the two intervals don't intersect, return "NO".


    [input/output] samples:
    intersection((1, 2), (2, 3)) ==> "NO"
    intersection((-1, 1), (0, 4)) ==> "NO"
    intersection((-3, -1), (-5, 5)) ==> "YES"
    
    Example solution:
    # line 1
    def is_prime(num):
        # line 2
        if num == 1 or num == 0:
            # line 3
            return False
        # line 4
        if num == 2:
            # line 5
            return True
        # line 6
        for i in range(2, num+1):
            # line 7
            if num%i == 0:
                # line 8
                return False
        # line 9
        return True
    # line 10
    l = max(interval1[0], interval2[0])
    # line 11
    r = min(interval1[1], interval2[1])
    # line 12
    length = r - l
    # line 13
    if length > 0 and is_prime(length):
        # line 14
        return "YES"
    # line 15
    return "NO"
    
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("6")
    # END OF SOLUTION

def check(candidate):

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate([],[])
    out = f.getvalue().strip('\n')

    assert "6" == out
    for i in range(0, 20):
        if i != 6:
            assert str(i) != out

if __name__ == '__main__':
    check(intersection)
