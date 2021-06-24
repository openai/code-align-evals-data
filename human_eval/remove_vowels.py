def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\\nghijklm")
    'bcdf\\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('zbcd')
    'zbcd'
    """

    return "".join([s for s in text if s not in ["a", "e", "i", "o", "u"]])



METADATA = {}


def check(candidate):
    assert candidate('') == ''
    assert candidate("abcdef\nghijklm") == 'bcdf\nghjklm'
    assert candidate('abcdef') == 'bcdf'
    assert candidate('aaaaa') == ''
    assert candidate('zbcd') == 'zbcd'

if __name__ == '__main__':
    check(remove_vowels)
