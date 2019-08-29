"""
It was proposed by Christian Goldbach that every odd composite number
can be written as the sum of a prime and twice a square.
    9 = 7 + 2*1^2
    15 = 7 + 2*2^2
    21 = 3 + 2*3^2
    25 = 7 + 2*3^2
    27 = 19 + 2*2^2
    33 = 31 + 2*1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of
a prime and twice a square?
"""


import math
import itertools
from primes import is_prime, get_primes


def is_goldbach(n):
    for p in get_primes(n):
        x = math.sqrt((n-p)/2)
        if int(x)==x:
            # n = p + 2*x^2
            return int(x)
    return None

def solution(show_result=False):
    for oc in itertools.count(3, step=2):
        if is_prime(oc):
            continue
        elif is_goldbach(oc):
            if show_result:
                x = is_goldbach(oc)
                p = oc - 2*x^2
                print('{0} = {1} + 2*{2}^2'.format(oc, p, x))
            continue
        else:
            return oc

if __name__=='__main__':
    print(solution(show_result=True))
