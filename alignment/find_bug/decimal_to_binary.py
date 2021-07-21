def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    
    Example solution:
    # line 1
    binary = bin(decimal)
    # line 2
    binary = "db" + binary
    # line 3
    binary = binary + "db"
    # line 4
    return binary
    
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("1")
    # END OF SOLUTION

def check(candidate):

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate(10)
    out = f.getvalue().strip('\n')

    assert "1" == out
    for i in range(0, 10):
        if i != 1:
            assert str(i) != out

if __name__ == '__main__':
    check(decimal_to_binary)
