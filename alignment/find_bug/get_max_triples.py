def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    
    Example solution:
    # line 1
    A = [i*i - i + 1 for i in range(1,n+1)]
    # line 2
    ans = []
    # line 3
    for i in range(n):
        # line 4
        for j in range(i+1,n):
            # line 5
            for k in range(j,n):
                # line 6
                if (A[i]+A[j]+A[k])%3 == 0:
                    # line 7
                    ans += [(A[i],A[j],A[k])]
    # line 8
    return len(ans)
    
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
    check(get_max_triples)
