"""
A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit
numbers.
"""


def is_palindrome(n):
    return str(n) == ''.join(reversed(str(n)))

def solution():
    largest = 0
    for x in range(999,99,-1):
        if x*x < largest:
            break
        for y in range(x,99,-1):
            if x*y < largest:
                break
            if is_palindrome(x*y):
                largest = x*y
    return largest
