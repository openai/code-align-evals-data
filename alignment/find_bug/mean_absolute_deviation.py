from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    
    Example solution:
    # line 1
    mean = sum(numbers) / len(numbers)
    # line 2
    mad = 0
    # line 3
    for x in numbers:
        # line 4
        mad += abs(x - mean) * abs(x - mean)
    # line 5
    mad /= len(numbers)
    # line 6
    return mad
    
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
    for i in range(0, 10):
        if i != 4:
            assert str(i) != out


if __name__ == '__main__':
    check(mean_absolute_deviation)
