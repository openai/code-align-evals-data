def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    
    Example solution:
    # line 1
    new_lst = []
    # line 2
    for word in sentence.split():
        # line 3
        flg = 0
        # line 4
        if len(word) == 1:
            # line 5
            flg = 1
        # line 6
        for i in range(1, len(word)):
            # line 7
            if len(word)%i == 0:
                # line 8
                flg = 1
        # line 9
        if flg == 0 or len(word) == 2:
            # line 10
            new_lst.append(word)
    # line 11
    return " ".join(new_lst)
    
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
        candidate('')
    out = f.getvalue().strip('\n')

    assert "6" == out
    for i in range(0, 15):
        if i != 6:
            assert str(i) != out

if __name__ == '__main__':
    check(words_in_sentence)
