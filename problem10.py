"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


from primes import get_primes

def solution(N=2000000):
    return sum(get_primes(N))
