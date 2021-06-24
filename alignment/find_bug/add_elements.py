def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the first k element that has at most two digits.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    
    Example solution:
    # line 1
    first_k_sum = 0
    # line 2
    for i in range(len(arr)):
        # line 3
        if len(str(arr[i])) <= 2:
            # line 4
            first_k_sum += arr[i];
    #line 5
    return first_k_sum
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print(2)
    # END OF SOLUTION

def check(candidate):
    
    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate([1, 2, 3, 4], 2)
    out = f.getvalue().strip('\n')

    assert "2" == out
    for i in range(0, 10):
        if i != 2:
            assert str(i) != out

if __name__ == '__main__':
    check(add_elements)
