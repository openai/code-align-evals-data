def tri(n):
    """Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
    the last couple centuries. However, what people don't know is Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    For example:
    tri(2) = 1 + (2 / 2) = 2
    tri(4) = 3
    tri(3) = tri(2) + tri(1) + tri(4)
           = 2 + 3 + 3 = 8 
    You are given a non-negative integer number n, you have to a return a list of the 
    first n + 1 numbers of the Tribonacci sequence.
    Examples:
    tri(3) = [1, 3, 2, 8]
    """

    if n == 0:
        return [1]
    my_tri = [1, 3]
    for i in range(2, n + 1):
        if i % 2 == 0:
            my_tri.append(i / 2 + 1)
        else:
            my_tri.append(my_tri[i - 1] + my_tri[i - 2] + (n + 3) / 2)
    return my_tri

def check(candidate):

    # Check some simple cases
    assert candidate(3) == [1, 3, 2.0, 8.0]
    assert candidate(4) == [1, 3, 2.0, 8.5, 3.0]
    assert candidate(5) == [1, 3, 2.0, 9.0, 3.0, 16.0]
    assert candidate(6) == [1, 3, 2.0, 9.5, 3.0, 17.0, 4.0]
    assert candidate(7) == [1, 3, 2.0, 10.0, 3.0, 18.0, 4.0, 27.0]
    assert candidate(8) == [1, 3, 2.0, 10.5, 3.0, 19.0, 4.0, 28.5, 5.0]
    assert candidate(9) == [1, 3, 2.0, 11.0, 3.0, 20.0, 4.0, 30.0, 5.0, 41.0]
    assert candidate(20) == [1, 3, 2.0, 16.5, 3.0, 31.0, 4.0, 46.5, 5.0, 63.0, 6.0, 80.5, 7.0, 99.0, 8.0, 118.5, 9.0, 139.0, 10.0, 160.5, 11.0]

    # Check some edge cases that are easy to work out by hand.
    assert candidate(0) == [1]
    assert candidate(1) == [1, 3]

if __name__ == '__main__':
    check(tri)
