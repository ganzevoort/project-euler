"""
The number 3797 has an interesting property. Being prime itself, it is
possible to continuously remove digits from left to right, and remain
prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from
left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

"""


from primes import is_prime, get_primes


def is_left_truncatable(p):
    while is_prime(p):
        if p < 10:
            return True
        p = int(str(p)[1:])
    return False

def right_truncatables():
    primes = list(get_primes(10))
    while primes:
        primes = filter(is_prime, (10*p+d for p in primes for d in (1,3,7,9)))
        for p in primes:
            yield p

def solution():
    return sum(filter(is_left_truncatable, right_truncatables()))
