from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
    Example solution:
    # line 1
    import collections
    # line 2
    c = collections.Counter(numbers)
    # line 3
    ret = []
    # line 4
    for n in numbers:
        # line 5
        if c[n] == 1:
            # line 6
            ret.append(n)
    # line 7
    return sorted(ret)
    
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("7")
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

    assert "7" == out
    for i in range(0, 10):
        if i != 7:
            assert str(i) != out


if __name__ == '__main__':
    check(remove_duplicates)
