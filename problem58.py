# -*- coding: utf-8 -*-
"""
Starting with 1 and spiralling anticlockwise in the following way,
a square spiral with side length 7 is formed.

        37 36 35 34 33 32 31
        38 17 16 15 14 13 30
        39 18  5  4  3 12 29
        40 19  6  1  2 11 28
        41 20  7  8  9 10 27
        42 21 22 23 24 25 26
        43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right
diagonal, but what is more interesting is that 8 out of the 13 numbers
lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square
spiral with side length 9 will be formed. If this process is continued,
what is the side length of the square spiral for which the ratio of
primes along both diagonals first falls below 10%?
"""


# Unsatisfied with the resulting2300ms I looked at how others solved this.
# On http://www.mathblog.dk/project-euler-58-primes-diagonals-spiral/
# Kristian introduced me to the Miller-Rabin primality test which brought it
# down to about 310ms. Wow.
from miller_rabin import is_prime
import itertools


# A square spiral with a side length L has size L^2, and the last number
# is in the bottom right corner. So, that's never prime.
#   bottom left has L^2 - (L-1)
#   top left has L^2 - 2*(L-1)
#   top right has L^2 - 3*(L-1)
# Number of numbers along both diagonals is 2*L-1.

def solution(verbose=False):
    primes = 0
    for L in itertools.count(3,2):
        corners = [L*L - (L-1)*i for i in (1,2,3)]
        primes += len(filter(is_prime, corners))
        ratio = 100.0 * primes / (2*L-1)
        if verbose:
            print "%5d: %5d/%5d = %6.3f" % (L, primes, 2*L-1, ratio)
        if ratio < 10.0:
            return L


if __name__=='__main__':
    print solution(verbose=True)
