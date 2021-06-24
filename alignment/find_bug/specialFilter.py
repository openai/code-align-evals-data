def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    
    Example solution:
    # line 1
    count = 0
    # line 2
    for num in nums:
        # line 3
        if num > 10:
            # line 4
            odd_digits = (1, 3, 5, 7, 9)
            # line 5
            number_as_string = str(num)
            # line 6
            if int(number_as_string[1]) in odd_digits and int(number_as_string[-1]) in odd_digits:
                # line 7
                count += 1
    # line 8
    return count 
    
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
        candidate([])
    out = f.getvalue().strip('\n')

    assert "6" == out
    for i in range(0, 10):
        if i != 6:
            assert str(i) != out

if __name__ == '__main__':
    check(specialFilter)
