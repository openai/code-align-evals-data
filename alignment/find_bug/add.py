def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
    Example solution:
    # line 1
    even_sum = 0
    # line 2
    for i in range(len(lst)):
        # line 3
        if i % 2 == 0 and lst[i] % 2 == 0:
            # line 4
            even_sum += lst[i]
    # line 5
    return even_sum
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("3")
    # END OF SOLUTION

def check(candidate):

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate([])
    out = f.getvalue().strip('\n')

    assert "3" == out
    for i in range(0, 10):
        if i != 3:
            assert str(i) != out

if __name__ == '__main__':
    check(add)
