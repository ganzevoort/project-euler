"""
The fraction 49/98 is a curious fraction, as an inexperienced
mathematician in attempting to simplify it may incorrectly believe that
49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction,
less than one in value, and containing two digits in the numerator
and denominator.

If the product of these four fractions is given in its lowest common
terms, find the value of the denominator.
"""

from primes import gcd

def mul(seq):
    product = 1
    for i in seq:
        product *= i
    return product


def solution():
    fractions = []
    for a in range(1,10):
        for b in range(1,10):
            for c in range(1,10):
                for d in range(1,10):
                    fraction = float(10*a+b) / (10*c+d)
                    if fraction >= 1.0:
                        continue
                    elif a==c and fraction == float(b)/d:
                        outn, outd = b, d
                    elif a==d and fraction == float(b)/c:
                        outn, outd = b, c
                    elif b==c and fraction == float(a)/d:
                        outn, outd = a, d
                    elif b==d and fraction == float(a)/c:
                        outn, outd = a, c
                    else:
                        continue
                    #print '{}{}/{}{} = {}/{}'.format(a,b,c,d, outn,outd)
                    fractions.append((outn, outd))
    #print fractions
    n, d = map(mul,zip(*fractions))
    g = gcd(n, d)
    n, d = n/g, d/g
    return d
