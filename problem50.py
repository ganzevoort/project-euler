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


class PrimeSequenceGenerator(object):
    def __init__(self, N):
        self.N = N
        self.primes = list(get_primes(N))

    def find_longest_sequence_value(self, start=0, min_length=1, result=None):
        """ result is best sofar, is sum(S) for some sequence S.
        Try and find a longer sequence, so min_length is len(S)+1.
        First try all sequences starting at start, then recurse with start+1.
        """
        subtotal = sum(self.primes[start : start + min_length])
        if subtotal >= self.N:
            # longer sequences starting at start or higher by definition yield
            # out-of-range results, so we're done here.
            return result
        for length in itertools.count(min_length):
            subtotal += self.primes[start+length]
            if subtotal >= self.N:
                # Can't find a better result at start, move up to start+1
                return self.find_longest_sequence_value(
                        start+1, min_length+1, result)
            if is_prime(subtotal):
                # Improvement: result=sum(S), length=len(S)
                min_length = length
                result = subtotal


def solution():
    N = 1000000
    generator = PrimeSequenceGenerator(N)
    return generator.find_longest_sequence_value()

