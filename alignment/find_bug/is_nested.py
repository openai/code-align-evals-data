def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if there is a valid square brackets inside another
    valid square brakets (in other words, it is nested) and False otherwise.
    A valid square brackets always should have a closing square bracket ']' after the 
    opening square bracket '['

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    
    Example solution:
    # line 1
    opening_bracket_index = []
    # line 2
    closing_bracket_index = []
    # line 3
    for i in range(len(string)):
        # line 4
        if string[i] == '[':
            # line 5
            opening_bracket_index.append(i)
        # line 6
        else:
            # line 7
            closing_bracket_index.append(i)
    # line 8
    closing_bracket_index.reverse()
    # line 9
    cnt = 0
    # line 10
    i = 0
    # line 11
    l = len(closing_bracket_index)
    # line 12
    for idx in opening_bracket_index:
        # line 13
        if i - 1 < l and idx < closing_bracket_index[i]:
            # line 14
            cnt += 1
            # line 15
            i += 1
    # line 16
    return cnt >= 2
    
    '''
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("13")
    # END OF SOLUTION

def check(candidate):

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate('')
    out = f.getvalue().strip('\n')

    assert "13" == out
    for i in range(0, 15):
        if i != 13:
            assert str(i) != out

if __name__ == '__main__':
    check(is_nested)
