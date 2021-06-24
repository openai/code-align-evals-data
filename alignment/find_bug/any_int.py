def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if the sum of any two numbers is equal to the third number, and all numbers are integers.
    Returns false in any other cases.
    
    Examples
    any_int(5, 2, 7) ➞ True
    
    any_int(3, 2, 2) ➞ False

    any_int(3, -2, 1) ➞ True
    
    any_int(3.6, -2.2, 2) ➞ False
  
    Example solution:
    # line 1
    if isinstance(x,int) and isinstance(y,int) and isinstance(x+y,int):
        # line 2
        if (x+y==z) or (x+z==y) or (y+z==x):
            # line 3
            return True
        # line 4
        return False
    # line 5
    return False
    
    '''
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("1")
    # END OF SOLUTION

def check(candidate):

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate(0, 0, 0)
    out = f.getvalue().strip('\n')

    assert "1" == out
    for i in range(0, 10):
        if i != 1:
            assert str(i) != out

if __name__ == '__main__':
    check(any_int)
