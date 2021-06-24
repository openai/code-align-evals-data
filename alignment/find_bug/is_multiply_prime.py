def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
    Example solution:
    # line 1
    def is_prime(n):
        # line 2
        for j in range(2,n+1):
            # line 3
            if i%j == 0:
                # line 4
                return False
        # line 5
        return True
    # line 6
    for i in range(2,101):
        # line 7
        if not is_prime(i): continue
        # line 8
        for j in range(2,101):
            # line 9
            if not is_prime(j): continue
            # line 10
            for k in range(2,101):
                # line 11
                if not is_prime(k): continue
                # line 12
                if i*j*k == a: return True
    # line 13
    return False
    
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("2")
    # END OF SOLUTION

def check(candidate):

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate(10)
    out = f.getvalue().strip('\n')

    assert "2" == out
    for i in range(0, 10):
        if i != 2:
            assert str(i) != out

if __name__ == '__main__':
    check(is_multiply_prime)
