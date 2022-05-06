"""
https://projecteuler.net/problem=76

Counting summations

Problem 76
It is possible to write five as a sum in exactly six different ways:

    4 + 1
    3 + 2
    3 + 1 + 1
    2 + 2 + 1
    2 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at
least two positive integers?
"""


import time
import functools


def solution1(N=100, verbose=False):
    """
    write N as a sum a0 + a1 + ... an
    with n > 0, 0 < a0 < N, 0 < ai <= a(i-1)
    recursion: pass in limit too:
    """
    @functools.lru_cache(maxsize=N*N)
    def ways(N, limit):
        if N == 0:
            return 1
        return sum(
            ways(N-a0, min(N-a0, a0))
            for a0 in range(1, limit+1)
        )

    t0 = time.time()
    result = ways(N, N-1)
    if verbose:
        print("s1 N={} {:8}ms result={}".format(
            N, int(1000*(time.time()-t0)), result))
    return result


solution = solution1


if __name__ == '__main__':
    solution1(verbose=3, N=5)
    for N in range(6,100):
        solution(verbose=True, N=N)
    solution(verbose=True)

