"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial
of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

import itertools
import math


fac = dict((x,math.factorial(x)) for x in range(10))

def combinations(length, prefix=[]):
    prefix_sum = sum(fac[d] for d in prefix)
    if len(prefix)==length:
        if map(int, sorted(str(prefix_sum))) == prefix:
            return [prefix_sum]
	return []
    elif len(str(prefix_sum)) > length:
        return []
    elif len(str(prefix_sum + (length - len(prefix)) * fac[9])) < length:
        return []
    results = []
    for d in range(prefix[-1] if prefix else 0, 10):
        results.extend(combinations(length, prefix + [d]))
    return results

def solution():
    # because 7*9! < 9999999, n has to b < 9999999
    return sum(sum(combinations(length)) for length in range(2,8))

