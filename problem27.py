"""
Euler published the remarkable quadratic formula:

    n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive
values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1)
+ 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is
clearly divisible by 41.

Using computers, the incredible formula  n^2 + 79n + 1601 was discovered,
which produces 80 primes for the consecutive values n = 0 to 79. The
product of the coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

    n^2 + an + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |4| = 4

Find the product of the coefficients, a and b, for the quadratic
expression that produces the maximum number of primes for consecutive
values of n, starting with n = 0.
"""


import itertools
from primes import is_prime, get_primes

def quadratics_length(a, b):
    for n in itertools.count(1):
        if not is_prime(n*n + a*n + b):
            return n

def solution():
    N = 1000
    best_length, best_a, best_b = 0, 0, 0
    # b can't be negative, and for n=0, it has to be a prime
    for b in reversed(list(get_primes(N))):
        # n^2 + an + b is a multiple of b if n==b,
        # so quadratics_length(a,b) <= b
        if b < best_length:
            break
        for a_abs in range(1,N,2):
            for a in (a_abs, -a_abs):
                if not is_prime(best_length*best_length + a*best_length + b):
                    # quadratics_length(a, b) <= best_length, so skip
                    continue
                length = quadratics_length(a, b)
                if length > best_length:
                    best_length, best_a, best_b = length, a, b
    return best_a * best_b
