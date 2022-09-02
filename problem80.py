"""
https://projecteuler.net/problem=80

Square root digital expansion
Problem 80
It is well known that if the square root of a natural number is not
an integer, then it is irrational. The decimal expansion of such
square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital
sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the
digital sums of the first one hundred decimal digits for all the
irrational square roots.
"""


import math


def hundred_decimal_digits_of_square_root(number):
    return sum(map(int, str(math.isqrt(number * 100**100))[:100]))


def has_irrational_square_root(number):
    return math.isqrt(number) !=  math.sqrt(number)


def solution(verbose=False):
    return sum(
        hundred_decimal_digits_of_square_root(number)
        for number in range(1,101)
        if has_irrational_square_root(number)
    )


if __name__ == '__main__':
    assert hundred_decimal_digits_of_square_root(2) == 475
    solution(verbose=2)
