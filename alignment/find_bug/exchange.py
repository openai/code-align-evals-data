def exchange(lst1, lst2):
    """In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return "YES".
    Otherwise, return "NO".
    For example:
    exchange([1, 2, 3, 4], [1, 2, 3, 4]) => "YES"
    exchange([1, 2, 3, 4], [1, 5, 3, 4]) => "NO"
    It is assumed that the input lists will be non-empty.
    
    Example solution:
    # line 1
    odd = 0
    # line 2
    even = 0
    # line 3
    for i in lst1:
        # line 4
        if i%2 == 1:
            # line 5
            odd += 1
    # line 6
    for i in lst2:
        # line 7
        if i%2 == 0:
            # line 8
            even += 1
    # line 9
    if even <= odd:
        # line 10
        return "YES"
    # line 11
    return "NO"
    
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
        candidate([], [])
    out = f.getvalue().strip('\n')

    assert "9" == out
    for i in range(0, 15):
        if i != 9:
            assert str(i) != out

if __name__ == '__main__':
    check(exchange)
