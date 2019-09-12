"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we
can see that the 6th prime is 13.

What is the 10 001st prime number?
"""


import itertools
from primes import get_primes


def solution(N=10001):
    return next(itertools.islice(get_primes(), N-1, N))


if __name__ == '__main__':
    print(list(itertools.islice(get_primes(), 0, 6)))
    print(solution(N=6))
    print(solution())
