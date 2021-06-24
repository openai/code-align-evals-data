def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}
    
    Example solution:
    # line 1
    dict1={}
    # line 2
    list1=test.split(" ")
    # line 3
    t=0
    # line 4
    for i in list1:
        # line 5
        if(list1.count(i)>t) and i!=' ':
            # line 6
            t=list1.count(i)
    # line 7
    if t>0:
        # line 8
        for i in list1:
            # line 9
            if(list1.count(i)==t):
                # line 10
                dict1[i]=t
    # line 11
    return dict1

    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("5")
    # END OF SOLUTION

def check(candidate):

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate('')
    out = f.getvalue().strip('\n')

    assert "5" == out
    for i in range(0, 10):
        if i != 5:
            assert str(i) != out

if __name__ == '__main__':
    check(histogram)
