def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    
    Example solution:
    # line 1
    count = 0
    # line 2
    for i in range(0,len(s)):
        # line 3
        if s[i] in "AEIOU":
            # line 4
            count += 1
    # line 5
    return count
    
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("2")
    # END OF SOLUTION

def check(candidate):

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate('')
    out = f.getvalue().strip('\n')

    assert "2" == out
    for i in range(0, 10):
        if i != 2:
            assert str(i) != out
    assert True

if __name__ == '__main__':
    check(count_upper)
