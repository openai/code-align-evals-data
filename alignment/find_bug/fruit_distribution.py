def fruit_distribution(s,n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.
    for examble:
    fruit_distribution("5 apples and 6 oranges", 19) ->19 - 5 + 6 = 8
    fruit_distribution("0 apples and 1 oranges",3) -> 3 - 0 + 1 = 2
    fruit_distribution("2 apples and 3 oranges", 100) -> 100 - 2 + 3 = 95
    fruit_distribution("100 apples and 1 oranges",120) -> 120 - 100 + 1 = 19
    
    Example solution:
    # line 1
    lis = list()
    # line 2
    for i in s.split(' '):
        # line 3
        if s.isdigit():
            # line 4
            lis.append(int(i))
    # line 5
    return n - sum(lis)
    
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("3")
    # END OF SOLUTION

def check(candidate):

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate('', 1)
    out = f.getvalue().strip('\n')

    assert "3" == out
    for i in range(0, 10):
        if i != 3:
            assert str(i) != out


if __name__ == '__main__':
    check(fruit_distribution)
