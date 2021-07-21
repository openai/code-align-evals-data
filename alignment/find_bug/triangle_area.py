def triangle_area(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.
    Example:
    triangle_area(3, 4, 5) == 6.00
    triangle_area(1, 2, 10) == -1
    
    Example solution:
    # line 1
    if a + b < c or a + c < b or b + c < a:
        # line 2
        return -1
    # line 3
    s = (a + b + c)/2
    # line 4    
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    # line 5
    area = round(area, 2)
    # line 6
    return area
    
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
        candidate(1, 2, 3)
    out = f.getvalue().strip('\n')

    assert "1" == out
    for i in range(0, 10):
        if i != 1:
            assert str(i) != out

if __name__ == '__main__':
    check(triangle_area)
