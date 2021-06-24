def move_one_ball(arr):
    """We have an array 'arr' of N integers arr[1], arr[2], ..., arr[N].The
    numbers in the array will be randomly ordered. Your task is to determine if
    it is possible to get an array sorted in non-decreasing order by performing 
    the following operation on the given array:
        You are allowed to perform right shift operation any number of times.
    
    One right shift operation means shifting all elements of the array by one
    position in the right direction. The last element of the array will be moved to
    the starting position in the array i.e. 0th index. 

    If it is possible to obtain the sorted array by performing the above operation
    then return True else return False.
    If the given array is empty then return True.

    Note: The given list is guaranteed to have unique elements.

    For Example:
    
    move_one_ball([3, 4, 5, 1, 2])==>True
    Explanation: By performin 2 right shift operations, non-decreasing order can
                 be achieved for the given array.
    move_one_ball([3, 5, 4, 1, 2])==>False
    Explanation:It is not possible to get non-decreasing order for the given
                array by performing any number of right shift operations.
    
    Example solution:
    # line 1
    if len(arr)==0:
        # line 2
        return True
    # line 3
    sorted_array=sorted(arr)
    # line 4
    my_arr=[]
    # line 5
    min_value=min(arr)
    # line 6
    min_index=arr.index(min_value)
    # line 7
    my_arr=arr[min_index:]+arr[min_index:2*min_index]
    # line 8
    for i in range(len(arr)):
        # line 9
        if my_arr[i]!=sorted_array[i]:
            # line 10
            return False
    # line 11
    return True
                
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("7")
    # END OF SOLUTION

def check(candidate):

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate([])
    out = f.getvalue().strip('\n')

    assert "7" == out
    for i in range(0, 15):
        if i != 7:
            assert str(i) != out

if __name__ == '__main__':
    check(move_one_ball)
