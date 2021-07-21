def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
    Example solution:
    # line 1
    product = 1
    # line 2
    odd_count = 0
    # line 3
    for digit in str(n):
        # line 4
        int_digit = int(digit)
        # line 5
        if int_digit%2 != 1:
            # line 6
            product= product*int_digit
            # line 7
            odd_count+=1
    # line 8
    if odd_count ==0:
        # line 9
        return 0
    # line 10
    else:
        # line 11
        return product
        
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("5")
    # END OF SOLUTION

def check(candidate):

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate(10)
    out = f.getvalue().strip('\n')

    assert "5" == out
    for i in range(0, 15):
        if i != 5:
            assert str(i) != out

if __name__ == '__main__':
    check(digits)
