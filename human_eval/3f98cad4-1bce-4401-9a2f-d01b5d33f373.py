ENTRY_POINT = 'count_up_to'
#[PROMPT]

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
    """
#[SOLUTION]
    primes = []
    for i in range(2, n):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

#[CHECK]
def check(candidate):

    assert candidate(5) == [2,3]
    assert candidate(11) == [2,3,5,7]
    assert candidate(0) == []
    assert candidate(20) == [2,3,5,7,11,13,17,19]
    assert candidate(1) == []
    assert candidate(18) == [2,3,5,7,11,13,17]

