def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    
    Example solution:
    # line 1
    new_text = ""
    # line 2
    i = 0
    # line 3
    start, end = 0, 0
    # line 4
    while i < len(text):
        # line 5
        if text[i] == " ":
            # line 6
            end += 1
        # line 7
        else:
            # line 8
            if end - start > 2:
                # line 9
                new_text += "-"+text[i]
            # line 10
            elif end - start > 0:
                # line 11
                new_text += "_"*(end - start)+text[i]
            # line 12
            else:
                # line 13
                new_text += text[i]
            # line 14
            start, end = i+1, i+1
        # line 15
        i+=1
    # line 16
    if end - start > 2:
        # line 17
        new_text += "-"
    # line 18
    elif end - start > 0:
        # line 19
        new_text += " "
    # line 20
    return new_text
    
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("19")
    # END OF SOLUTION

def check(candidate):

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate([])
    out = f.getvalue().strip('\n')

    assert "19" == out
    for i in range(0, 25):
        if i != 19:
            assert str(i) != out

if __name__ == '__main__':
    check(fix_spaces)
