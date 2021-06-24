def can_arange(arr):
    """Create a function which returns the index of the element such that after 
    removing that element the remaining array is itself sorted in ascending order.
    If the given array is already sorted in ascending order then return -1.
    Note: It is guaranteed that the array arr will either be sorted or it will
          have only one element such that after its removal the given array
          will become sorted in ascending order.
          - The given array will not contain duplicate values.
    Examples:
    can_arange([1,2,4,3,5]) = 3
    can_arange([1,2,3]) = -1
    
    Example solution:
    # line 1
    ind=0
    # line 2
    i=1;
    # line 3
    while i<len(arr):
      # line 4
      if arr[i]<arr[i-1]:
        # line 5
        ind=i
      # line 6
      i+=1
    # line 7
    return ind
    
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("1")
    # END OF SOLUTION

def check(candidate):
    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate([])
    out = f.getvalue().strip('\n')

    assert "1" == out
    for i in range(0, 10):
        if i != 1:
            assert str(i) != out

if __name__ == '__main__':
    check(can_arange)
