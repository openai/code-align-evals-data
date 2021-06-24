def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    
    Example solution:
    # line 1
    suf = ['txt', 'exe', 'dll']
    # line 2
    lst = file_name.split(sep='.')
    #  line 3
    if len(lst) != 2:
        # line 4
        return 'No'
    # line 5
    if not lst[1] in suf:
        # line 6
        return 'No'
    # line 7
    if len(lst[0]) == 0:
        # line 8
        return 'No'
    # line 9
    if lst[0][0].isalpha():
        # line 10
        return 'No'
    # line 11
    t = len([x for x in lst[0] if x.isdigit()])
    # line 12
    if t > 3:
        # line 13
        return 'No'
    # line 14
    return 'Yes'
    
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
        candidate([])
    out = f.getvalue().strip('\n')

    assert "9" == out
    for i in range(0, 20):
        if i != 9:
            assert str(i) != out


if __name__ == '__main__':
    check(file_name_check)
