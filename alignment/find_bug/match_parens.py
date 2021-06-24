def match_parens(lst):
    '''
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all parentheses in S
    are balanced. For example: the string '(())()' is good, while the string
    '())' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    match_parens(['()(', ')']) == 'Yes'
    match_parens([')', ')']) == 'No'
    
    Example solution:
    # line 1
    def check(s):
        # line 2
        val = 0
        # line 3
        for i in s:
            # line 4
            if i == '(':
                # line 5
                val = val + 1
            # line 6
            else:
                # line 7
                val = val - 1
        # line 8
        return True if val == 0 else False
    # line 9
    S1 = lst[0] + lst[1]
    # line 10
    S2 = lst[1] + lst[0]
    # line 11
    return 'No' if check(S1) or check(S2) else 'Yes'
    
    '''
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("11")
    # END OF SOLUTION

def check(candidate):

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate([])
    out = f.getvalue().strip('\n')

    assert "11" == out
    for i in range(0, 15):
        if i != 11:
            assert str(i) != out

if __name__ == '__main__':
    check(match_parens)
