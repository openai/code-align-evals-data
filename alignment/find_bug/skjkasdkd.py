def skjkasdkd(lst):
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.

    Examples:
    For lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3] the output should be 10
    For lst = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1] the output should be 25
    For lst = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3] the output should be 13
    For lst = [0,724,32,71,99,32,6,0,5,91,83,0,5,6] the output should be 11
    For lst = [0,81,12,3,1,21] the output should be 3
    For lst = [0,8,1,2,1,7] the output should be 7
    
    Example solution:
    # line 1
    def isPrime(n):
        # line 2
        for i in range(2,int(n**0.5)+1):
            # line 3
            if n%i==0:
                # line 4
                return False
        # line 5
        return True
    # line 6
    maxx = 0
    # line 7
    i = 0
    # line 8
    while i <= len(lst):
        # line 9
        if(lst[i] > maxx and isPrime(lst[i])):
            # line 10
            maxx = lst[i]
        # line 11
        i+=1
    # line 12
    result = sum(int(digit) for digit in str(maxx))
    # line 13
    return result
    
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("8")
    # END OF SOLUTION

def check(candidate):

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate([])
    out = f.getvalue().strip('\n')

    assert "8" == out
    for i in range(0, 15):
        if i != 8:
            assert str(i) != out

if __name__ == '__main__':
    check(skjkasdkd)
