"""
An irrational decimal fraction is created by concatenating the positive
integers:

    0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value
of the following expression.

    d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
"""


import itertools


def champernowne_digit(n):
    # 1 2 3 ...
    # 10 11 12 13 ...
    # 100 101 102 103 ...
    n -= 1  # indexing starting at 0 is easier
    for length in itertools.count(1):
        offset = pow(10,length-1)
        size = 9 * offset * length
        if n >= size:
            n -= size
        else:
            return str(n/length + offset)[n%length]

def mul(seq):
    product = 1
    for i in seq:
        product *= i
    return product

def solution():
    return mul(int(champernowne_digit(i))
               for i in (1, 10, 100, 1000, 10000, 100000, 1000000))

