# [PROMPT]


def count_distinct_characters(string: str) -> int:
    """Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # [SOLUTION]

    return len(set(string).lower())


# [CHECK]
def check(candidate):
    assert candidate("abcde") == 5
    assert candidate("abcde" + "cade" + "CADE") == 5
    assert candidate("aaaaAAAAaaaa") == 1
    assert candidate("Jerry jERRY JeRRRY") == 5


if __name__ == "__main__":
    check(count_distinct_characters)
