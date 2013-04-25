"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

import itertools

def solution():
    N = 5
    # n >= 10 or else it's not a sum
    # digit <= 9, so digit^N <= 9^N (6561 for N=4)
    # if n has l digits, then 10^(l-1) <= n < 10^l,
    # but also n <= l * 9^N, so 10^(l-1) <= l * 9^N
    # if l <= 9 then certainly l-1 <= N+1, or l <= N+2
    total = 0
    for l in itertools.count(2):
        lwb = pow(10, l-1)
        upb1 = pow(10, l)
        upb2 = l*pow(9, N)
        while lwb < upb2 < upb1:
            # check first digit of upb2:
            d = int(str(upb2)[0])
            upb3 = (l-1)*pow(9,N) + pow(d,N)
            if upb3 >= upb2:
                break
            upb2 = upb3
        upb = min(upb1, upb2)
        if upb <= lwb:
            return total
        for n in range(lwb, upb):
            if n == sum(pow(int(d),N) for d in str(n)):
                total += n
