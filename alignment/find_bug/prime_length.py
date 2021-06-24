def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    
    Example solution:
    # line 1
    l = len(string)
    # line 2
    if l == 0 or l == 1:
        # line 3
        return False
    # line 4
    for i in range(1, l):
        # line 5
        if l % i == 0:
            # line 6
            return False
    # line 7
    return True
    
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("4")
    # END OF SOLUTION

def check(candidate):

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate('')
    out = f.getvalue().strip('\n')

    assert "4" == out
    for i in range(0, 10):
        if i != 4:
            assert str(i) != out


if __name__ == '__main__':
    check(prime_length)
