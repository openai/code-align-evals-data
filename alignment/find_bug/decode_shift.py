def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    
    Example solution:
    # line 1
    decoded_str = ''
    # line 2
    for ch in s:
        # line 3
        v = (ord(ch) - 5 - ord('a'))
        # line 4
        v = (v + ord('a'))
        # line 5
        decoded_str += chr(v)
    # line 6
    return decoded_str
    
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("3")
    # END OF SOLUTION


METADATA = {}


def check(candidate):
    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate('')
    out = f.getvalue().strip('\n')

    assert "3" == out
    for i in range(0, 10):
        if i != 3:
            assert str(i) != out

if __name__ == '__main__':
    check(decode_shift)
