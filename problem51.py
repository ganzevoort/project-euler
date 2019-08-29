"""
By replacing the 1st digit of the 2-digit number *3, it turns out that six
of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this
5-digit number is the first example having seven primes among the ten
generated numbers, yielding the family: 56003, 56113, 56333, 56443,
56663, 56773, and 56993. Consequently 56003, being the first member of
this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not
necessarily adjacent digits) with the same digit, is part of an eight
prime value family.
"""


# I experimented with miller-rabin.is_prime, but for this problem
# prefetch_primes wins
from primes import is_prime, prefetch_primes


def family(pattern):
    digits = '123456789' if pattern[0]=='*' else '0123456789'
    return list(filter(is_prime, [int(pattern.replace('*',d)) for d in digits]))


class Solver(object):
    def __init__(self, N):
        self.N = N
        self.best_sofar = None

    def check(self, pattern):
        f = family(pattern)
        if len(f) != self.N:
            return False
        this = f[0]
        if not self.best_sofar or self.best_sofar > this:
            self.best_sofar = this
        return True

    def all_patterns(self, prefix='', suffix_length=1):
        if suffix_length==0:
            if '*' in prefix:
                yield prefix
            return
        if not prefix:
            prefetch_primes(int('9'*suffix_length))
        digits = '*0123456789' if prefix else '*123456789'

        if prefix and self.best_sofar:
            pattern = prefix + '*'*suffix_length
            lwb = int(pattern.replace('*', '1' if pattern[0]=='*' else '0'))
            if self.best_sofar < lwb:
                #print('%d < %s %d' % (self.best_sofar, pattern, lwb))
                return

        for d in digits:
            for p in self.all_patterns(prefix + d, suffix_length-1):
                yield p
        if self.best_sofar:
            return
        if not prefix:
            for p in self.all_patterns(suffix_length=suffix_length+1):
                yield p

def solution():
    solver = Solver(N=8)
    for pattern in solver.all_patterns():
        if solver.check(pattern):
            pass  # print(pattern, family(pattern))

    return solver.best_sofar

