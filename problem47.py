"""
The first two consecutive numbers to have two distinct prime factors are:
    14 = 2 x 7
    15 = 3 x 5

The first three consecutive numbers to have three distinct prime
factors are:
    644 = 2^2 x 7 x 23
    645 = 3 x 5 x 43
    646 = 2 x 17 x 19.

Find the first four consecutive integers to have four distinct prime
factors. What is the first of these numbers?
"""


import itertools
from primes import get_primes, prime_divisors


def solution(N=4, show_result=False):
    sequence = []
    for n in itertools.count(1):
        if len(set(prime_divisors(n)))==N:
            sequence.append(n)
            if len(sequence)==N:
                if show_result:
                    for n in sequence:
                        print '{0} = {1}'.format(n,
                                'x'.join(map(str,list(prime_divisors(n)))))
                return sequence[0]
        else:
            sequence = []


if __name__=='__main__':
    for N in range(1,5):
        print solution(N=N, show_result=True)
