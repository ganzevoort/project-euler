"""
https://projecteuler.net/problem=70

Totient permutation

Problem 70
Euler's Totient function, φ(n) [sometimes called the phi function],
is used to determine the number of positive numbers less than or
equal to n which are relatively prime to n. For example, as 1, 2,
4, 5, 7, and 8, are all less than nine and relatively prime to nine,
φ(9)=6.

The number 1 is considered to be relatively prime to every positive
number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a
permutation of 79180.

Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation
of n and the ratio n/φ(n) produces a minimum.
"""


import time
import math
from primes import prime_divisors, get_primes
from problem69 import phi


# Like in problem 69, this solution is too slow.
# Digest https://en.wikipedia.org/wiki/Euler's_totient_function to
# find a better approach.
def solution1(N=10000000, verbose=False):
    result = None
    totient = None
    if verbose:
        print('      time        n     φ(n)  n/φ(n)    divisors')
        print('------------------------------------------------')
    t0 = time.time()
    for n in range(2, N):
        phi_n = phi(n)
        if sorted(str(n)) == sorted(str(phi_n)):
            if verbose:
                t1 = time.time()
                print("{:8}ms {:8} {:8}  {:.4f}    {}".format(
                    int(1000*(t1-t0)), n, phi_n, n/phi_n,
                    list(prime_divisors(n))))
            if not totient or n/phi_n < totient:
                result = n
                totient = n/phi_n
    if verbose:
        t1 = time.time()
        print("{:8}ms {} {}".format(
                    int(1000*(t1-t0)), result, totient))
    return result


def solution2(N=10000000, verbose=False):
    # n should probably be a product of only a few primes.
    # n cannot be prime itself, because then φ(n) == n-1 is not a
    # permutation of n.
    # If p is the smallest prime divisor of n, then φ(n) is close to
    # n*(1-1/p), so n/φ(n) is close to 1+1/(p-1). To minimise that
    # n should be a product of higher primes.
    # Further more, if we've found a result with low n/φ(n), further
    # candidates should have a lowest prime divisor of at least
    # 1/(1-1/result)
    result = None
    totient = None
    if verbose:
        print('      time        n     φ(n)  n/φ(n)       lp  divisors')
        print('-------------------------------------------------------')
    t0 = time.time()
    lowest_prime = None
    for p in get_primes(N):
        if lowest_prime and p < lowest_prime:
            continue
        for q in get_primes(min(p, N//p)):
            if lowest_prime and q < lowest_prime:
                continue
            n = p*q
            phi_n = phi(n)
            if sorted(str(n)) == sorted(str(phi_n)):
                if not totient or n/phi_n < totient:
                    result = n
                    totient = n/phi_n
                    lowest_prime = math.ceil(1/(1-1/totient))
                    if verbose:
                        t1 = time.time()
                        print("{:8}ms {:8} {:8}  {:.4f} {:8}  {}".format(
                            int(1000*(t1-t0)), n, phi_n, n/phi_n,
                            lowest_prime,
                            list(prime_divisors(n))))
    if verbose:
        t1 = time.time()
        print("{:8}ms {} {}".format(
                    int(1000*(t1-t0)), result, totient))
    return result


def solution3(N=10000000, verbose=False):
    #from primes import prefetch_primes
    #prefetch_primes(N)
    # solution2 tried to minimise the search space, but still too
    # much time is spent calculating φ(n).
    # If n == p*q, where p and q are prime, then φ(n) is the length
    # of all numbers up to n minus the numbers divisible by p or q,
    # so:
    #       phi_n = n + 1 - p - q if p != q else n - p
    result = None
    totient = 2.0
    if verbose:
        print('      time        n     φ(n)  n/φ(n)       lp  divisors')
        print('-------------------------------------------------------')
    t0 = time.time()
    lowest_prime = 2
    for p in reversed(list(get_primes(int(math.sqrt(N))))):
        if p < lowest_prime:
            break
        for q in reversed(list(get_primes(N // p))):
            if q < p:
                break
            n = p*q
            phi_n = n + 1 - p - q if p != q else n - p
            if n/phi_n < totient:
                if sorted(str(n)) == sorted(str(phi_n)):
                    result = n
                    totient = n/phi_n
                    lowest_prime = math.ceil(1/(1-1/totient))
                    if verbose:
                        t1 = time.time()
                        print("{:8}ms {:8} {:8}  {:.4f} {:8}  {}".format(
                            int(1000*(t1-t0)), n, phi_n, n/phi_n,
                            lowest_prime,
                            list(prime_divisors(n))))
    if verbose:
        t1 = time.time()
        print("{:8}ms {} {}".format(
                    int(1000*(t1-t0)), result, totient))
    return result


solution = solution3


if __name__ == '__main__':
    print(solution3(N=10000000, verbose=True))
    print(solution2(N=100000, verbose=True))
    print(solution1(N=1000, verbose=True))
