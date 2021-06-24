def eat(number, need, remaining):
    """Beastiality
    You're a hungry beast,and you already have eaten acertain number of animals,
    and now you need to eat another certain number of animals to complete the day's meals.
    you should return an array of [ total number of eaten animals,
                                    the number of animals left ]
    if no enough remaining animals, you will eat all, but you will still hungry :)
    
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
        the number of remaining animals thet exist in stock
    
    Constrain:
    * 0 <= number <= 1000
    * 0 <= need <= 1000
    * 0 <= remaining <= 1000

    Have fun :)
    """

    if(need <= remaining):
        return [ number + need , remaining-need ]
    else:
        return [ number + remaining , 0]

def check(candidate):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(5, 6, 10) == [11, 4], "Error"
    assert candidate(4, 8, 9) == [12, 1], "Error"
    assert candidate(1, 10, 10) == [11, 0], "Error"
    assert candidate(2, 11, 5) == [7, 0], "Error"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate(4, 5, 7) == [9, 2], "Error"
    assert candidate(4, 5, 1) == [5, 0], "Error"

if __name__ == '__main__':
    check(eat)
