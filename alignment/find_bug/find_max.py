def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
    Example solution:
    # line 1
    words.sort()
    # line 2
    ret = ''
    # line 3
    max_len = 0
    # line 4
    for word in words:
        # line 5
        if len(set(word)) >= max_len:
            # line 6
            max_len = len(set(word))
            # line 7
            ret = word
    # line 8
    return ret
    
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
        candidate([])
    out = f.getvalue().strip('\n')

    assert "5" == out
    for i in range(0, 10):
        if i != 5:
            assert str(i) != out
            
            
if __name__ == '__main__':
    check(find_max)
