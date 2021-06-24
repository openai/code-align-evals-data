def get_odd_collatz(n):
    """
    Given a positive integer n, return a sorted list that has the odd numbers in collatz sequence.

    The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined
    as follows: start with any positive integer n. Then each term is obtained from the 
    previous term as follows: if the previous term is even, the next term is one half of 
    the previous term. If the previous term is odd, the next term is 3 times the previous
    term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.

    Note: 
        1. Collatz(1) is [1].
        2. returned list sorted in increasing order.

    For example:
    get_odd_collatz(5) returns [1, 5] # The collatz sequence for 5 is [5, 16, 8, 4, 2, 1], so the odd numbers are only 1, and 5.
    
    Example solution:
    # line 1
    if n%2==0:
        # line 2
        odd_collatz = []
    # line 3
    else:
        # line 4
        odd_collatz = [n]
    # line 5
    while n > 1:
        # line 6
        if n % 2 == 0:
            # line 7
            n = n/2
        # line 8
        else:
            # line 9
            n = n*3 + 1
        # line 10
        if n%2 == 1:
            # line 11
            odd_collatz.append(int(n))
    # line 12
    return odd_collatz
    
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("12")
    # END OF SOLUTION

def check(candidate):

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate(10)
    out = f.getvalue().strip('\n')

    assert "12" == out
    for i in range(0, 15):
        if i != 12:
            assert str(i) != out

if __name__ == '__main__':
    check(get_odd_collatz)
