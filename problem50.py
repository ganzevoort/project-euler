"""
The prime 41, can be written as the sum of six consecutive primes:

    41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below
one-hundred.  The longest sum of consecutive primes below one-thousand
that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""


import itertools
from primes import is_prime, get_primes


def solution(N=1000000, verbose=False):
    primes = list(get_primes(N))

    S = []
    # result is best sofar, is sum(S) for some sequence S.
    # Try and find a longer sequence
    for start in itertools.count(0):
        subtotal = sum(primes[start : start + len(S)])
        if subtotal >= N:
            # longer sequences starting at start or higher by definition yield
            # out-of-range results, so we're done here.
            return sum(S)
        for length in itertools.count(len(S) + 1):
            subtotal += primes[start + length - 1]
            if subtotal >= N:
                # Can't find a better result at start, move up to start+1
                break
            if is_prime(subtotal):
                # Improvement
                S = primes[start : start + length]
                if verbose:
                    print('{} = {} ({})'.format(sum(S), S, len(S)))


if __name__ == '__main__':
    print(solution(N=1000, verbose=True))
