"""
A permutation is an ordered arrangement of objects. For example, 3124
is one possible permutation of the digits 1, 2, 3 and 4. If all of
the permutations are listed numerically or alphabetically, we call it
lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

    012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2,
3, 4, 5, 6, 7, 8 and 9?
"""

from itertools import islice, permutations
from math import factorial

def solution():
    N=1000000
    digits = '0123456789'
    #return ''.join(next(islice(permutations(digits), N-1, N)))
    # that was too easy, let's find the solution ourselves
    chosen = ''
    N -= 1  # easier to calculate with base 0
    while True:
        if len(digits)==1:
            chosen += digits
            return chosen
        # after choosing a first digit, (len(digits)-1)! options remain
        f = factorial(len(digits)-1)
        i = N / f
        chosen += digits[i]
        digits = digits[:i] + digits[i+1:]
        N %= f
