def my_func():
    a = 0
    a += 4
    # Please copy the line above three times, then return a.
    # END OF CONTEXT
    a += 4
    a += 4
    a += 4
    return a
    # END OF SOLUTION


def check(candidate):
    assert candidate() == 16


if __name__ == "__main__":
    check(my_func)