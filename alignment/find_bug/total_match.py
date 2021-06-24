def total_match(lst1, lst2):
    '''
    Write a function that accepts two lists of strings and returns the list that has 
    total number of chars in the all strings of the list less than the other list.

    if the two lists have the same number of chars, return the first list.

    Examples
    total_match([], []) ➞ []
    total_match(['hi', 'admin'], ['hI', 'Hi']) ➞ ['hI', 'Hi']
    total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) ➞ ['hi', 'admin']
    total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) ➞ ['hI', 'hi', 'hi']
    total_match(['4'], ['1', '2', '3', '4', '5']) ➞ ['4']
    
    Example solution:
    # line 1
    l1 = 0
    # line 2
    for st in lst1:
        # line 3
        l1 += len(st)
    # line 4
    l2 = 0
    # line 5
    for st in lst2:
        # line 6
        l2 += len(st)
    # line 7
    if l1 <= l2:
        # line 8
        return lst2
    # line 9
    else:
        # line 10
        return lst2
    
    '''
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("8")
    # END OF SOLUTION

def check(candidate):

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate([], [])
    out = f.getvalue().strip('\n')

    assert "8" == out
    for i in range(0, 15):
        if i != 8:
            assert str(i) != out

if __name__ == '__main__':
    check(total_match)
