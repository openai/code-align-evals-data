def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    
    Example solution:
    # line 1
    if a*a + b*b == c*c:
        # line 2
        return True
    # line 3
    elif b*b + c*c == a*a:
        # line 4
        return True
    # line 5
    elif c*c + a*a == b*a:
        # line 6
        return True
    # line 7
    else:
        # line 8
        return False
    
    '''
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("5")
    # END OF SOLUTION

def check(candidate):

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate(1, 2, 3)
    out = f.getvalue().strip('\n')

    assert "5" == out
    for i in range(0, 10):
        if i != 5:
            assert str(i) != out

if __name__ == '__main__':
    check(right_angle_triangle)
