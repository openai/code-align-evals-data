ENTRY_POINT = 'incr_list'
#[PROMPT]


def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
#[SOLUTION]
    return [(e + 1) for e in l]
#[CHECK]


METADATA = {}


def check(candidate):
    assert candidate([1, 2, 3]) == [2, 3, 4]
    assert candidate([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]

