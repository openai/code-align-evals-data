# [PROMPT]

from typing import List


def all_prefixes(string: str) -> List[str]:
    """Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # [SOLUTION]

    result = []

    for i in range(len(string)):
        result.append(string[:i])
    return result


# [CHECK]


def check(candidate):
    assert candidate("") == []
    assert candidate("asdfgh") == ["a", "as", "asd", "asdf", "asdfg", "asdfgh"]
    assert candidate("WWW") == ["W", "WW", "WWW"]


if __name__ == "__main__":
    check(all_prefixes)
