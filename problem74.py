"""
https://projecteuler.net/problem=74

Digit factorial chains

Problem 74
The number 145 is well known for the property that the sum of the
factorial of its digits is equal to 145:

    1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest
chain of numbers that link back to 169; it turns out that there are
only three such loops that exist:

    169 → 363601 → 1454 → 169
    871 → 45361 → 871
    872 → 45362 → 872

It is not difficult to prove that EVERY starting number will
eventually get stuck in a loop. For example,

    69 → 363600 → 1454 → 169 → 363601 (→ 1454)
    78 → 45360 → 871 → 45361 (→ 871)
    540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but
the longest non-repeating chain with a starting number below one
million is sixty terms.

How many chains, with a starting number below one million, contain
exactly sixty non-repeating terms?
"""


import time
import math


factorials = [math.prod(range(1,x+1)) for x in range(10)]


def sumfac(n):
    return sum(factorials[int(digit)] for digit in str(n))


def chain(n):
    seen = []
    while n not in seen:
        seen.append(n)
        n = sumfac(n)
    return seen


def solution1(N=1000000, verbose=False):
    t0 = time.time()
    maxchaincount = 0
    maxchainlength = 0
    for n in range(1,N):
        length = len(chain(n))
        if length > maxchainlength:
            maxchainlength = length
            maxchaincount = 1
        elif length == maxchainlength:
            maxchaincount += 1
    result = maxchaincount
    if verbose:
        t1 = time.time()
        print("s1: {:8}ms N={} result={}".format(int(1000*(t1-t0)), N, result))
    return result


_chainlength = {}
def chainlength(n):
    start_n = n
    seen = []
    while n not in seen:
        if n in _chainlength:
            length = _chainlength[n]
            for x in reversed(seen):
                length += 1
                _chainlength[x] = length
            return _chainlength[start_n]
        seen.append(n)
        n = sumfac(n)
    for i, x in enumerate(reversed(seen)):
        _chainlength[x] = i + 1
    loop = chain(n)
    for x in loop:
        _chainlength[x] = len(loop)
    return _chainlength[start_n]


def solution2(N=1000000, verbose=False):
    t0 = time.time()
    maxchaincount = 0
    maxchainlength = 0
    for n in range(1,N):
        length = chainlength(n)
        if length > maxchainlength:
            maxchainlength = length
            maxchaincount = 1
        elif length == maxchainlength:
            maxchaincount += 1
    result = maxchaincount
    if verbose:
        t1 = time.time()
        print("s2: {:8}ms N={} result={}".format(int(1000*(t1-t0)), N, result))
    return result


solution = solution2


if __name__ == '__main__':
    for n in (145, 169, 363601, 1454):
        print(n, '→', sumfac(n))
    for n in (169,):
        print(n, chain(n), chainlength(n))
    solution2(verbose=True)
    solution1(verbose=True)
