def eat(number, need, remaining):
    """
    You're a hungry beast,and you already have eaten a certain number of animals,
    and now you need to eat another certain number of animals to complete the day's meals.
    you should return an array of [ total number of eaten animals,
                                    the number of animals left ]
    if not enough remaining animals, you will eat all
    
    Example:
    * eat(5, 6, 10) -> [11, 4]
    * eat(4, 8, 9) -> [12, 1]
    * eat(1, 10, 10) -> [11, 0]
    * eat(2, 11, 5) -> [7, 0]
    
    Variables:
    @number : integer
        the number of animals that you have eaten.
    @need : integer
        the number of animals that you need to eat.
    @remaining : integer
        the number of remaining animals that exist in stock
    
    Constraints:
    * 0 <= number <= 1000
    * 0 <= need <= 1000
    * 0 <= remaining <= 1000

    
    Example solution:
    # line 1
    if(need <= remaining):
        # line 2
        return [ remaining + need , remaining-need ]
    # line 3
    else:
        # line 4
        return [ number + remaining , 0]
    
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("2")
    # END OF SOLUTION

def check(candidate):

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate(1, 2, 3)
    out = f.getvalue().strip('\n')

    assert "2" == out
    for i in range(0, 10):
        if i != 2:
            assert str(i) != out

if __name__ == '__main__':
    check(eat)
