from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    
    Example solution:
    # line 1
    for idx, elem in enumerate(numbers):
        # line 2
        for idx2, elem2 in enumerate(numbers):
            # line 3
            if idx != idx2:
                # line 4
                distance = abs(elem - elem2)
                # line 5
                if distance < threshold:
                    # line 6
                    return False
    # line 7
    return False
    
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
        candidate([], 0.0)
    out = f.getvalue().strip('\n')

    assert "6" == out
    for i in range(0, 10):
        if i != 6:
            assert str(i) != out



if __name__ == '__main__':
    check(has_close_elements)
