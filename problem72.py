"""
https://projecteuler.net/problem=72

Counting fractions

Problem 72
Consider the fraction, n/d, where n and d are positive integers.
If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending
order of size, we get:

    1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7,
    3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper
fractions for d ≤ 1,000,000?
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

def solution1(N=1000000, verbose=False):
    t0 = time.time()
    result = len(reduced_proper_fractions(N))
    if verbose:
        t1 = time.time()
        print("s1: {:8}ms N={} result={}".format(int(1000*(t1-t0)), N, result))
    return result


def solution2(N=1000000, verbose=False):
    t0 = time.time()
    # simple inlining,
    # don't look at what the fractions are,
    # don't sort
    result = len([
            1
            for d in range(2,N+1)
            for n in range(1,d)
            if HCF(n,d)==1
            ])
    if verbose:
        t1 = time.time()
        print("s2: {:8}ms N={} result={}".format(int(1000*(t1-t0)), N, result))
    return result


def phi(n):
    # problem69.phi is a slower implementation
    # https://en.wikipedia.org/wiki/Euler%27s_totient_function#Computing_Euler's_totient_function
    factors = set(prime_divisors(n))
    # tried:
    #   n * math.prod(f-1 for f in factors) // math.prod(factors)
    # but that isn't faster
    x = n
    for f in factors:
        x = (x * (f-1) ) // f
    return x


def solution3(N=1000000, verbose=False):
    t0 = time.time()
    # first, count factors without reducing:
    #   1/8, 2/8, 3/8, 4/8, 5/8, 6/8, 7/8   -> 7: N-1
    #   1/7, 2/7, 3/7, ...       6/7        -> 6: N-2
    #   ...
    #   1/3, 2/3                            -> 2
    #   1/2                                 -> 1
    # that's sum(1..N-1) = N*(N-1) / 2
    # now count, excluding reducable fractions:
    #   1/8, 3/8, 5/8, 7/8                  -> 4
    #   1/7, 2/7, 3/7, 4/7, 5/7, 6/7        -> 6
    #   1/6, 5/6                            -> 2
    #   1/5, 2/5, 3/5, 4/5                  -> 4
    #   1/4, 3/4                            -> 2
    #   1/3, 2/3                            -> 2
    #   1/2                                 -> 1
    # so, for each denominator d, remove the numarators n,
    # where n is a multiple of the prime factors of d,
    # or, equivalently, HCF(n,d) != 1
    # these are relative primes, or φ(d) as we've seen in problem69
    result = sum(phi(d) for d in range(2, N+1))
    if verbose:
        t1 = time.time()
        print("s3: {:8}ms N={} result={}".format(int(1000*(t1-t0)), N, result))
    return result


solution = solution3


if __name__ == '__main__':
    print("N=8: [{}]".format(
        " ".join(map(str, reduced_proper_fractions(N=8)))))
    solution(N=8, verbose=True)
    for solution in solution3, solution2, solution1:
        N = 8
        t0 = time.time()
        while True:
            solution(N, verbose=True)
            if time.time() - t0 > 1.0:
                break
            N *= 2
            if N > 1e12:
                break
