from typing import List

def below_zero(operations: List[int]) -> bool:
    """You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account falls below zero, and
    at that point the function should return True. Otherwise it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    """
    # line 1
    balance = 0

    # line 2
    for op in operations:

        # line 3
        balance = op

        # line 4
        if balance < 0:

            # line 5
            return True
    # line 6
    return False

    # Please print out which line of the above program contains an error. E.g. "line 4"
    # END OF CONTEXT
    print("line 3")
    # END OF SOLUTION


def check(candidate):
    import inspect

    source = inspect.getsource(candidate)
    lines = source.strip().split("\n")
    # remove comments
    lines = [l for l in lines if l.strip() != "" and l.strip()[0] != "#"]
    assert lines[-1] == '    print("line 3")'


if __name__ == "__main__":
    check(below_zero)