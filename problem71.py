"""
https://projecteuler.net/problem=71

Ordered fractions

Problem 71
Consider the fraction, n/d, where n and d are positive integers.
If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending
order of size, we get:

    1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7,
    3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ≤ 1,000,000
in ascending order of size, find the numerator of the fraction
immediately to the left of 3/7.
"""


import time
import math
from fractions import Fraction
from primes import gcd as HCF


def reduced_proper_fractions(N):
    return sorted(
            Fraction(n, d)
            for d in range(2,N+1)
            for n in range(1,d)
            if HCF(n,d)==1
    )


def solution1(N=1000000, verbose=False):
    t0 = time.time()
    target = Fraction(3, 7)
    rpf = reduced_proper_fractions(N)
    left_sibling = rpf[rpf.index(target) - 1]
    if verbose:
        t1 = time.time()
        print("s1: {:8}ms N={} {}".format(
            int(1000*(t1-t0)),
            N,
            left_sibling))
    return left_sibling.numerator


def solution2(N=1000000, verbose=False):
    t0 = time.time()
    target = Fraction(3, 7)
    candidates = []
    for d in range(N, 1, -1):
        if d != target.denominator:
            n = math.floor(target * d)
            if HCF(n, d)==1:
                candidates.append(Fraction(n, d))
    left_sibling = max(candidates)
    if verbose:
        t1 = time.time()
        print("s2: {:8}ms N={} {}".format(
            int(1000*(t1-t0)),
            N,
            left_sibling))
    return left_sibling.numerator


def solution3(N=1000000, verbose=False):
    t0 = time.time()
    target = Fraction(3, 7)
    # assume na/da, with
    #       0 < da <= N-7, na = floor(da*3/7)
    # is the best approximation of 3/7, then:
    #       na/da < (na+3)/(da+7) < 3/7
    # so, nb/db = (na+3)/(da+7) is a better approximation,
    # and db <= N
    # so, the best approximation is n/d with:
    #       N-7 < d <= N, n = floor(d*3/7)
    candidates = []
    for d in range(N, N-7, -1):
        if d != target.denominator:
            n = math.floor(target * d)
            if HCF(n, d)==1:
                candidates.append(Fraction(n, d))
    left_sibling = max(candidates)
    if verbose:
        t1 = time.time()
        print("s3: {:8}ms N={} {}".format(
            int(1000*(t1-t0)),
            N,
            left_sibling))
    return left_sibling.numerator


solution = solution3


if __name__ == '__main__':
    print("N=8: [{}]".format(
        " ".join(map(str, reduced_proper_fractions(N=8)))))
    solution1(N=8, verbose=True)
    solution2(N=8, verbose=True)
    solution3(N=8, verbose=True)
    for solution in solution1, solution2, solution3:
        N = 10
        t0 = time.time()
        while True:
            solution(N, verbose=True)
            if time.time() - t0 > 0.1:
                break
            N *= 10
            if N > 1e12:
                break
    print(solution())
