def compare(game,guess):
    """I think we all remember that feeling when the result of some long-awaited
    event is finally known. The feelings and thoughts you have at that moment are
    definitely worth noting down and comparing.
    Your task is to compare if a person guessed correctly the results of the matches.
    You are given two arrays of scores and guesses, each index shows a game. If they have guessed correctly,
    return 0, and if they did not guessed return how many numbers they have missed or added extra.
    
    
    example:

    compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) -> [0,0,0,0,3,3]
    compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) -> [4,4,1,0,0,6]
    
    Example solution:
    # line 1
    result = []
    # line 2
    for i in range(len(game)):
        # line 3
        diff = guess[i] - game[i]
        # line 4
        result.append(diff)
    # line 5
    return result
    
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
        candidate([], [])
    out = f.getvalue().strip('\n')

    assert "3" == out
    for i in range(0, 10):
        if i != 3:
            assert str(i) != out

if __name__ == '__main__':
    check(compare)
