ENTRY_POINT = 'remove_vowels'

FIX = """
Make vowel check case insensitive.
"""


#[PROMPT]


def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """
#[SOLUTION]
    return "".join([s for s in text if s.lower() not in ["a", "e", "i", "o", "u"]])
#[CHECK]


METADATA = {}


def check(candidate):
    assert candidate('') == ''
    assert candidate("abcdef\nghijklm") == 'bcdf\nghjklm'
    assert candidate('abcdef') == 'bcdf'
    assert candidate('aaaaa') == ''
    assert candidate('aaBAA') == 'B'
    assert candidate('zbcd') == 'zbcd'

