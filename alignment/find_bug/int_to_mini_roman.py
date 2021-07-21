def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    
    Example solution:
    # line 1
    num = [1, 4, 5, 9, 10, 40, 50, 90,  
           100, 400, 500, 900, 1000] 
    # line 2
    sym = ["I", "IV", "V", "IX", "X", "XL",  
           "L", "XC", "C", "CD", "D", "CM", "M"] 
    # line 3
    i = 12
    # line 4
    res = ''
    # line 5
    while number:
        # line 6 
        div = number // num[i]
        # line 7 
        number %= num[i]
        # line 8 
        while div:
            # line 9 
            res += sym[1]
            # line 10 
            div -= 1
        # line 11
        i -= 1
    # line 12
    return res.lower()
    
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("9")
    # END OF SOLUTION

def check(candidate):

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate(10)
    out = f.getvalue().strip('\n')

    assert "9" == out
    for i in range(0, 15):
        if i != 9:
            assert str(i) != out

if __name__ == '__main__':
    check(int_to_mini_roman)
