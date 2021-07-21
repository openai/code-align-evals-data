def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True
    
    Example solution:
    # line 1
    l = len(b)
    # line 2
    pat = b + b
    # line 3
    for i in range(len(a) - l + 1):
        # line 4
        for j in range(l, l + 1):
            # line 5
            if a[i:i+l] == pat[j:j+l]:
                # line 6
                return True
    # line 7
    return False
    
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("4")
    # END OF SOLUTION
    
def check(candidate):

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate('', '')
    out = f.getvalue().strip('\n')

    assert "4" == out
    for i in range(0, 10):
        if i != 4:
            assert str(i) != out

if __name__ == '__main__':
    check(cycpattern_check)
