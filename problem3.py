"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from primes import prime_divisors


def solution():
    N = 600851475143
    return prime_divisors(N)[-1]
