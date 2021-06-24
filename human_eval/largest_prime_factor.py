def largest_prime_factor(n: int):
    """Return the largest prime factor of n.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    def is_prime(k):
        if k < 2:
            return False
        for i in range(2, k - 1):
            if k % i == 0:
                return False
        return True
    largest = 1
    for j in range(2, n):
        if n % j == 0 and is_prime(j):
            largest = max(largest, j)
    return largest



METADATA = {}


def check(candidate):
    assert candidate(13195) == 29
    assert candidate(2048) == 2

if __name__ == '__main__':
    check(largest_prime_factor)
