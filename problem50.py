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

    def sequence(self, length):
        for index in range(len(self.primes) + 1 - length):
            sequence = self.primes[index : index + length]
            value = sum(sequence)
            if value >= self.N:
                break
            yield value

    def find_a_value(self, length):
        for value in self.sequence(length):
            return value

    def find_longest_sequence_value(self):
        lwb, upb = 1, 2
        while self.find_a_value(upb):
            lwb = upb
            upb *= 2
        while upb != lwb+1:
            length = (lwb + upb) / 2
            if self.find_a_value(length):
                lwb=length
            else:
                upb=length
        for length in range(lwb, 1, -1):
            for value in self.sequence(length):
                if is_prime(value):
                    return value


def solution():
    N = 1000000
    generator = PrimeSequenceGenerator(N)
    return generator.find_longest_sequence_value()

