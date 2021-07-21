def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
    Example solution:
    # line 1
    if not s:
        # line 2
        return []
    # line 3
    s_list = []
    # line 4
    for letter in s:
        # line 5
        if letter == ',':
            # line 6
            s_list.append(',')
        # line 7
        else:
            # line 8
            s_list.append(letter)
    # line 9
    s_list = "".join(s_list)
    # line 10
    return s_list.split()
    
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("6")
    # END OF SOLUTION

def check(candidate):

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate('')
    out = f.getvalue().strip('\n')

    assert "6" == out
    for i in range(0, 15):
        if i != 6:
            assert str(i) != out

if __name__ == '__main__':
    check(words_string)
