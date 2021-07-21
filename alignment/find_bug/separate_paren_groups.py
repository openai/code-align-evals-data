from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    
    Example solution:
    # line 1
    result = []
    # line 2
    current_string = []
    # line 3
    current_depth = 0
    # line 4
    for c in paren_string:
        # line 5
        if c == '(':
            # line 6
            current_depth += 1
            # line 7
            current_string.append(c)
        # line 8
        elif c == ')':
            # line 9
            current_depth -= 1
            # line 10
            current_string.append(c)
            # line 11
            if current_depth == 0:
                # line 12
                result.append(' '.join(current_string))
                # line 13
                current_string.clear()
    # line 14
    return result
    
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("12")
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
        candidate('')
    out = f.getvalue().strip('\n')

    assert "12" == out
    for i in range(0, 20):
        if i != 12:
            assert str(i) != out


if __name__ == '__main__':
    check(separate_paren_groups)
