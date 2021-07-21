def string_to_md5(text):
    """
    Given a string 'test', return its md5 hash equivalent string.
    If text is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    
    Example solution:
    # line 1
    import hashlib
    # line 2
    if len(text) <= 1:
        # line 3
        return None
    # line 4
    encoded = text.encode('ascii')
    # line 5
    hashed = hashlib.md5(encoded).hexdigest()
    # line 6
    return hashed
    
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
        candidate('')
    out = f.getvalue().strip('\n')

    assert "2" == out
    for i in range(0, 10):
        if i != 2:
            assert str(i) != out

if __name__ == '__main__':
    check(string_to_md5)
