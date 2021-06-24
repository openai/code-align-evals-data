def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,15,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,15,17]
    
    Example solution:
    # line 1
    primes = []
    # line 2
    for i in range(2, n):
        # line 3
        is_prime = True
        # line 4
        for j in range(1, i):
            # line 5
            if i % j == 0:
                # line 6
                is_prime = False
                # line 7
                break
        # line 8
        if is_prime:
            # line 9
            primes.append(i)
    # line 10
    return primes
    
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
        candidate(1)
    out = f.getvalue().strip('\n')

    assert "4" == out
    for i in range(0, 10):
        if i != 4:
            assert str(i) != out

if __name__ == '__main__':
    check(count_up_to)
