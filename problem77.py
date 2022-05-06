"""
https://projecteuler.net/problem=77

Prime summations

Problem 77
It is possible to write ten as the sum of primes in exactly five
different ways:

    7 + 3
    5 + 5
    5 + 3 + 2
    3 + 3 + 2 + 2
    2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes
in over five thousand different ways?
"""


import time
import itertools
import functools
from primes import get_primes


def solution1(min_ways=5001, verbose=False):
    """
    write N as a sum a0 + a1 + ... an
    with n > 0, 0 < a0 < N, 0 < ai <= a(i-1)
    recursion: pass in limit too:
    """
    @functools.lru_cache(maxsize=1000)
    def ways(N, limit):
        if N == 0:
            return 1
        return sum(
            ways(N-a0, min(N-a0, a0))
            for a0 in get_primes(limit+1)
        )
    t0 = time.time()
    for N in itertools.count(4):
        num_ways = ways(N, N-1)
        if isinstance(verbose, int) and verbose > 1:
            print("s1 N={} {:8}ms ways={}".format(
                N, int(1000*(time.time()-t0)), num_ways))
        if num_ways >= min_ways:
            result = N
            break
    if verbose:
        print("s1 N={} {:8}ms result={}".format(
            N, int(1000*(time.time()-t0)), result))
        print(ways.cache_info())
    return result


solution = solution1


if __name__ == '__main__':
    solution(verbose=3, min_ways=5)
    solution(verbose=True)

