def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    
    Example solution:
    # line 1
    if len(word) < 3:
        # line 2
        return ""
    # line 3
    vowels = {"a", "e", "i", "o", "u", "A", "E", 'O', 'U', 'I'}
    # line 4
    for i in range(len(word)-2, 0, -1):
        # line 5
        if word[i] in vowels:
            # line 6
            if (word[i+1] not in vowels) or (word[i-1] not in vowels):
                # line 7
                return word[i]
    # line 8
    return ""
    
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("6")
    # END OF SOLUTION

def check(candidate):

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate([])
    out = f.getvalue().strip('\n')

    assert "6" == out
    for i in range(0, 10):
        if i != 6:
            assert str(i) != out

if __name__ == '__main__':
    check(get_closest_vowel)
