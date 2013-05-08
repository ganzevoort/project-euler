"""
We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once; for example, the 5-digit number, 15234,
is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to
only include it once in your sum.  """


import itertools


def solution():
    digits = '123456789'
    products = set()
    def check(A,B):
        C = A * B
        if ''.join(sorted(str(A) + str(B) + str(C))) == digits:
            products.add(C)
            #print '{} x {} = {}'.format(A, B, C)

    # A x B  = C
    # assume A < B
    # if len(A) >= 3 and len(B) >= 3 then len(C) >= 5, too long
    # same if len(A) >= 2 and len(B) >= 4 or len(A) >= 1 and len(B) >= 5
    # if len(A) <= 2 and len(B) <= 2 then len(C) <= 4, too short
    # same if len(A) <= 1 and len(B) <= 3
    # so len(A)==1 and len(B)==4, therefore len(C)==4,
    # or len(A)==2 and len(B)==3, therefore len(C)==4.
    for attempt in itertools.permutations(digits, 5):
        check(int(''.join(attempt[:1])), int(''.join(attempt[1:])))
        check(int(''.join(attempt[:2])), int(''.join(attempt[2:])))
    return sum(products)
