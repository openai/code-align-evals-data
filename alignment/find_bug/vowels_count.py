def vowels_count(s):
    """Write a function smallLetterCount which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    
    Example solution:
    # line 1
    vowels = "aeiouAEIOU"
    # line 2
    n_vowels = sum(c in vowels for c in s)
    # line 3
    if s[-1] == 'y':
        # line 4
        n_vowels += 1
    # line 5
    return n_vowels
    
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
        candidate('')
    out = f.getvalue().strip('\n')

    assert "3" == out
    for i in range(0, 10):
        if i != 3:
            assert str(i) != out

if __name__ == '__main__':
    check(vowels_count)
