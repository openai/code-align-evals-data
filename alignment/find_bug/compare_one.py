def compare_one(a, b):
    """
    Create a function that takes integer, float or string, reprepresenting
    a real numbers, and returns the larger variable in a given variable type.
    Return None if the values are equal.
    Note: if float represented as a string, the floating point might be . or ,

    compare_one(1, 2.5) ➞ 2.5
    compare_one(1, "2,3") ➞ "2,3"
    compare_one("5,1", "6") ➞ "6"
    compare_one("1", 1) ➞ None
    
    Example solution:
    # line 1
    temp_a, temp_b = a, b
    # line 2
    if isinstance(temp_a, str): temp_a = temp_a.replace(',','.')
    # line 3
    if isinstance(temp_b, str): temp_b = temp_b.replace(',','.')
    # line 4
    if float(temp_a) <= float(temp_b): return None
    # line 5
    return a if float(temp_a) > float(temp_b) else b 
    
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
        candidate("", "")
    out = f.getvalue().strip('\n')

    assert "4" == out
    for i in range(0, 10):
        if i != 4:
            assert str(i) != out

if __name__ == '__main__':
    check(compare_one)
