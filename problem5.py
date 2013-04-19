"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""

from primes import lcm


def solution():
    N = 20
    x = 2
    for y in range(3,N+1):
        x = lcm(x,y)
    return x
