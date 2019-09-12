"""
A Pythagorean triplet is a set of three natural numbers, a < b < c,
for which,

    a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def solution(N=1000):
    for a in range(1, N):
        for b in range(a+1, N):
            c = N - a-b
            if c <= b:
                break
            if a*a + b*b == c*c:
                return a*b*c
