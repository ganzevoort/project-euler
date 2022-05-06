"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


import time
from primes import get_primes
from pyprimesieve import primes_sum


def solution1(N=2000000):
    return sum(get_primes(N))


def solution2(N=2000000):
    return primes_sum(N)


solution = solution2


if __name__ == '__main__':
    for solution in solution2, solution1:
        N = 10
        while True:
            t0 = time.time()
            result = solution(N)
            t1 = time.time()
            print("{}: {:8}ms N={} result={}".format(
                solution.__name__,
                int(1000*(t1-t0)), N, result))
            if time.time() - t0 > 1.0:
                break
            N *= 10
            if N > 1e12:
                break
