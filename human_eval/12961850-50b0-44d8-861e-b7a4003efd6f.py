ENTRY_POINT = 'int_to_mini_roman'
#[PROMPT]

def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
#[SOLUTION]
    num = [1, 4, 5, 9, 10, 40, 50, 90,  
           100, 400, 500, 900, 1000] 
    sym = ["I", "IV", "V", "IX", "X", "XL",  
           "L", "XC", "C", "CD", "D", "CM", "M"] 
    i = 12
    res = ''
    while number: 
        div = number // num[i] 
        number %= num[i] 
        while div: 
            res += sym[i] 
            div -= 1
        i -= 1
    return res.lower()
#[CHECK]
def check(candidate):

    # Check some simple cases
    assert candidate(19) == 'xix'
    assert candidate(152) == 'clii'
    assert candidate(251) == 'ccli'
    assert candidate(426) == 'cdxxvi'
    assert candidate(500) == 'd'
    assert candidate(1) == 'i'
    assert candidate(43) == 'xliii'
    assert candidate(532) == 'dxxxii'

    # Check some edge cases that are easy to work out by hand.
    assert True

