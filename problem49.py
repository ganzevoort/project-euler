"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
increases by 3330, is unusual in two ways: (i) each of the three terms
are prime, and, (ii) each of the 4-digit numbers are permutations of
one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
primes, exhibiting this property, but there is one other 4-digit
increasing sequence.

What 12-digit number do you form by concatenating the three terms in
this sequence?
"""


from itertools import permutations, combinations, combinations_with_replacement
from primes import is_prime, get_primes


def unusual_sequence(digits):
    primes = list(filter(is_prime, set((int(''.join(p)) for p in permutations(digits)))))
    if len(primes) < 3:
        return None
    primes.sort()
    for i0 in range(len(primes)):
        for i1 in range(i0+1, len(primes)):
            for i2 in range(i1+1, len(primes)):
                if primes[i2] - primes[i1] == primes[i1] - primes[i0]:
                    return [primes[i0], primes[i1], primes[i2]]

def solution(show_result=False):
    # seed prime factory
    digits = '123456789'
    list(get_primes(10000))
    for attempt in combinations_with_replacement(digits, 4):
        sequence = unusual_sequence(attempt)
        if sequence:
            if show_result:
                print(sequence)
            if sequence[0]!=1487:
                return ''.join(map(str, sequence))
    pass

if __name__=='__main__':
    print(solution(show_result=True))
