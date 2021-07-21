def bf(planet1, planet2):
    '''
    There are eight planets in our solar system: the closest to the Sun 
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2. 
    The function should return a tuple containing all planets whose orbits are 
    located between the orbit of planet1 and the orbit of planet2, sorted by 
    the proximity to the sun. 
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names. 
    Examples
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus")
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    
    Example solution:
    # line 1
    planet_names = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    # line 2
    if planet1 not in planet_names or planet2 not in planet_names or planet1 == planet2:
        # line 3
        return ()
    # line 4
    planet1_index = planet_names.index(planet1)
    # line 5
    planet2_index = planet_names.index(planet2)
    # line 6
    if planet1_index < planet2_index:
        # line 7
        return (planet_names[planet2_index + 1: planet1_index])
    # line 8
    else:
        # line 9
        return (planet_names[planet2_index + 1 : planet1_index])
    
    '''
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("7")
    # END OF SOLUTION

def check(candidate):
    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate("", "")
    out = f.getvalue().strip('\n')

    assert "7" == out
    for i in range(0, 10):
        if i != 7:
            assert str(i) != out

if __name__ == '__main__':
    check(bf)
