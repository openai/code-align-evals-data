def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
    Example solution:
    # line 1
    ret = ""
    # line 2
    for i in range(len(string)):
        # line 3
        if string[i].isupper():
            # line 4
            ret += string[i].lower()
        # line 5
        elif string[i].islower():
            # line 6
            ret = string[i].upper()
        # line 7
        else:
            # line 8
            ret += string[i]
    # line 9
    return ret
    
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("6")
    # END OF SOLUTION


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate([])
    out = f.getvalue().strip('\n')

    assert "6" == out
    for i in range(0, 10):
        if i != 6:
            assert str(i) != out
    
if __name__ == '__main__':
    check(flip_case)
