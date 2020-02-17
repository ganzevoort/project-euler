"""
https://projecteuler.net/problem=73

Counting fractions in a range

Problem 73
Consider the fraction, n/d, where n and d are positive integers.
If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending
order of size, we get:

    1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7,
    3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of
reduced proper fractions for d ≤ 12,000?
"""


import time
import math
from fractions import Fraction
from primes import gcd as HCF, prime_divisors


def reduced_proper_fractions(N):
    return sorted(
            Fraction(n, d)
            for d in range(2,N+1)
            for n in range(1,d)
            if HCF(n,d)==1
    )

def solution1(N=12000, verbose=False):
    t0 = time.time()
    rpf = reduced_proper_fractions(N)
    result = rpf.index(Fraction(1,2)) - rpf.index(Fraction(1,3)) - 1
    if verbose:
        t1 = time.time()
        print("s1: {:8}ms N={} result={}".format(int(1000*(t1-t0)), N, result))
    return result


def solution2(N=12000, verbose=False):
    t0 = time.time()
    # simple inlining
    lwb, upb = Fraction(1,3), Fraction(1,2)
    result = len([
            1
            for d in range(2,N+1)
            for n in range(1,d)
            if lwb < Fraction(n,d) < upb and HCF(n,d)==1
            ])
    if verbose:
        t1 = time.time()
        print("s2: {:8}ms N={} result={}".format(int(1000*(t1-t0)), N, result))
    return result


def solution3(N=12000, verbose=False):
    t0 = time.time()
    lwb, upb = Fraction(1,3), Fraction(1,2)
    result = 0
    for d in range(2,N+1):
        for n in range(math.floor(d*lwb)+1, math.ceil(d*upb)):
            if HCF(n,d)==1:
                result += 1
    if verbose:
        t1 = time.time()
        print("s3: {:8}ms N={} result={}".format(int(1000*(t1-t0)), N, result))
    return result


solution = solution3


if __name__ == '__main__':
    print("N=8: [{}]".format(
        " ".join(map(str, reduced_proper_fractions(N=8)))))
    for solution in solution3, solution2, solution1:
        solution(N=8, verbose=True)
    for solution in solution3, solution2, solution1:
        solution(N=1000, verbose=True)
    solution3(N=12000, verbose=True)
