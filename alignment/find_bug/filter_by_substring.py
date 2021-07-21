from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    
    Example solution:
    # line 1
    result = []
    # line 2
    for s in strings:
        # line 3
        if s in substring:
            # line 4
            result.append(s)
    # line 5
    return result
    
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("3")
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
        candidate([], '')
    out = f.getvalue().strip('\n')

    assert "3" == out
    for i in range(0, 10):
        if i != 3:
            assert str(i) != out

if __name__ == '__main__':
    check(filter_by_substring)
