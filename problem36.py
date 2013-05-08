"""
The decimal number, 585 = 1001001001 (binary), is palindromic in both
bases.

Find the sum of all numbers, less than one million, which are palindromic
in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""


import itertools


def binary_palindromic(n):
    bin_digits = bin(n)[2:]  # strip off leading '0b'
    return bin_digits == ''.join(reversed(bin_digits))

def decimal_palindromes(max):
    for length in itertools.count(1):
        half_length = (length+1)/2
        x = pow(10,half_length-1)
        # starting digit should be odd, as result has to be odd
        for d in range(1,10,2):
            for half in range(d*x, (d+1)*x):
                half = str(half)
                mirror = ''.join(reversed(half))
                if length%2==1:
                    mirror = mirror[1:]
                number = int(half + mirror)
                if number >= max:
                    return
                yield number


def solution():
    N = 1000000
    return sum(filter(binary_palindromic, decimal_palindromes(N)))
