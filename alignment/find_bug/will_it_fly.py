def will_it_fly(q,w):
    '''
    Write a function that returns True if an object will fly, False otherwise.
    The object will fly if it's balanced and the sum of the weight is less than or equal the maximum possible weight w.

    Example:
    will_it_fly([1, 2], 5) ➞ False 
    # 1+2 is less than the maximum possible weight, but it's unbalanced.

    will_it_fly([3, 2, 3], 1) ➞ False
    # it's balanced, but 3+2+3 is more than the maximum possible weight.

    will_it_fly([3, 2, 3], 9) ➞ True
    # 3+2+3 is less than the maximum possible weight, and it's balanced.

    will_it_fly([3], 5) ➞ True
    # 3 is less than the maximum possible weight, and it's balanced.
    
    Example solution:
    # line 1
    if sum(q) > w:
        # line 2
        return False
    # line 3
    i, j = 0, len(q)
    # line 4
    while i<j:
        # line 5
        if q[i] != q[j]:
            # line 6
            return False
        # line 7
        i+=1
        # line 8
        j-=1
    # line 9
    return True
    
    '''
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("3")
    # END OF SOLUTION

def check(candidate):

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate([], 2)
    out = f.getvalue().strip('\n')

    assert "3" == out
    for i in range(0, 10):
        if i != 3:
            assert str(i) != out

if __name__ == '__main__':
    check(will_it_fly)
