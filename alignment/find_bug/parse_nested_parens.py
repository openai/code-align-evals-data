from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
    Example solution:
    # line 1
    def parse_paren_group(s):
        # line 2
        depth = 0
        # line 3
        max_depth = 0
        # line 4
        for c in s:
            # line 5
            if c == '(':
                # line 6
                depth += 1
                # line 7
                max_depth = max(depth, max_depth)
            # line 8
            else:
                # line 9
                depth -= 1
        # line 10
        return max_depth - 1
    # line 11
    return [parse_paren_group(x) for x in paren_string.split(' ') if x]
    
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("10")
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

    assert "10" == out
    for i in range(0, 10):
        if i != 10:
            assert str(i) != out


if __name__ == '__main__':
    check(parse_nested_parens)
