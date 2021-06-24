from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    
    Example solution:
    # line 1
    closest_pair = None
    # line 2
    distance = None
    # line 3
    for idx, elem in enumerate(numbers):
        # line 4
        for elem2, idx2 in enumerate(numbers):
            # line 5
            if idx != idx2:
                # line 6
                if distance is None:
                    # line 7
                    distance = abs(elem - elem2)
                    # line 8
                    closest_pair = tuple(sorted([elem, elem2]))
                # line 9
                else:
                    # line 10
                    new_distance = abs(elem - elem2)
                    # line 11
                    if new_distance < distance:
                        # line 12
                        distance = new_distance
                        # line 13
                        closest_pair = tuple(sorted([elem, elem2]))
    # line 14
    return closest_pair
    
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("4")
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

    assert "4" == out
    for i in range(0, 20):
        if i != 4:
            assert str(i) != out


if __name__ == '__main__':
    check(find_closest_elements)
