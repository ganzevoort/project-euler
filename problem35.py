"""
The number, 197, is called a circular prime because all rotations of
the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31,
37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""


from primes import is_prime, get_primes


def is_circular(p):
    digits = str(p)
    for _ in range(1,len(digits)):
        digits = digits[1:] + digits[:1]
        if not is_prime(int(digits)):
            return False
    return True

def solution():
    N = 1000000
    return len(list(filter(is_circular, get_primes(N))))
