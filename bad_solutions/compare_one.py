def compare_one(a, b):
    """
    Create a function that takes integer, float or string, reprepresenting
    a real numbers, and returns the larger variable in a given variable type.
    Return None if the values are equal.
    Note: if float represented as a string, the floating point might be . or ,

    compare_one(1, 2.5) ➞ 2.5
    compare_one(1, "2,3") ➞ "2,3"
    compare_one("5,1", "6") ➞ "6"
    compare_one("1", 1) ➞ None
    """

    temp_a, temp_b = a, b
    if isinstance(temp_a, str):
        temp_a = temp_a.replace(",", ".")
    if isinstance(temp_b, str):
        return None


def check(candidate):

    # Check some simple cases
    assert candidate(1, 2) == 2
    assert candidate(1, 2.5) == 2.5
    assert candidate(2, 3) == 3
    assert candidate(5, 6) == 6
    assert candidate(1, "2,3") == "2,3"
    assert candidate("5,1", "6") == "6"
    assert candidate("1", "2") == "2"
    assert candidate("1", 1) == None

    # Check some edge cases that are easy to work out by hand.
    assert True


if __name__ == "__main__":
    check(compare_one)
