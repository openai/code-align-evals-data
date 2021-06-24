def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
    Example solution:
    # line 1
    even_count = 0
    # line 2
    odd_count = 0
    # line 3
    for i in str(abs(num)):
        # line 4
        if int(i)%2==0:
            # line 5
            even_count +=1
        # line 6
        else:
            # line 7
            odd_count +=1
    # line 8
    return (odd_count, even_count)
    
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("8")
    # END OF SOLUTION

def check(candidate):

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate(1)
    out = f.getvalue().strip('\n')

    assert "8" == out
    for i in range(0, 10):
        if i != 8:
            assert str(i) != out

if __name__ == '__main__':
    check(even_odd_count)
