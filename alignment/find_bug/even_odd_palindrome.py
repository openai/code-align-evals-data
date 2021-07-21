def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Example 1:

        Input: 3
        Output: (1, 2)
        Explanation:
        Integer palindrome are 1, 2, 3. one of them is even, and two of them are odd.

    Example 2:

        Input: 12
        Output: (4, 6)
        Explanation:
        Integer palindrome are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. four of them are even, and 6 of them are odd.

    Note:
        1. 1 <= n <= 10^3
        2. returned tuple has the number of even and odd integer palindromes respectively.
    
    Example solution:
    # line 1
    def is_palindrome(n):
        # line 2
        return str(n) == str(n)[::-1]
    #line 3
    even_palindrome_count = 0
    # line 4
    odd_palindrome_count = 0
    #line 5
    for i in range(1, n):
        # line 6
        if i%2 == 1 and is_palindrome(i):
            # line 7
            odd_palindrome_count += 1
        # line 8
        elif i%2 == 0 and is_palindrome(i):
            # line 9
            even_palindrome_count += 1
    # line 10
    return (even_palindrome_count, odd_palindrome_count)
    
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
        candidate(1)
    out = f.getvalue().strip('\n')

    assert "5" == out
    for i in range(0, 15):
        if i != 5:
            assert str(i) != out

if __name__ == '__main__':
    check(even_odd_palindrome)
