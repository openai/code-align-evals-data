def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """

    return sum(range(n + 1))



METADATA = {}


def check(candidate):
    assert candidate(1) == 1
    assert candidate(5) == 15
    assert candidate(10) == 55
    assert candidate(30) == 465
    assert candidate(100) == 5050

if __name__ == '__main__':
    check(sum_to_n)
