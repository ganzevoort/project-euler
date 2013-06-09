"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made
up of each of the digits 0 to 9 in some order, but it also has a rather
interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way,
we note the following:
    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""


import itertools
import primes


def substringdivisible(n):  # n is a string or list of digits
    substrings = (int(''.join(n[i+1:i+4])) for i in range(7))
    divisors = primes.get_primes()
    return all(s % d == 0 for s,d in zip(substrings,divisors))

def solution2():
    # substringdivisible('1406357289')
    return sum(int(''.join(n))
               for n in itertools.permutations('0123456789')
               if n[0]!='0' and substringdivisible(n))


def solution():
    divisors = [2,3,5,7,11,13,17]
    def x(prefix, digits):
        if prefix and prefix[0]=='0':
            return 0
        elif len(prefix) > 3:
            if int(prefix[-3:]) % divisors[len(prefix)-4] != 0:
                return 0
        if digits:
            return sum(x(prefix+d, digits-set((d,))) for d in digits)
        else:
            return int(prefix)
    return x('', set('0123456789'))
