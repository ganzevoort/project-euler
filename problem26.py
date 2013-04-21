"""
A unit fraction contains 1 in the numerator. The decimal representation
of the unit fractions with denominators 2 to 10 are given:

    1/2 =   0.5
    1/3 =   0.(3)
    1/4 =   0.25
    1/5 =   0.2
    1/6 =   0.1(6)
    1/7 =   0.(142857)
    1/8 =   0.125
    1/9 =   0.(1)
    1/10    =   0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It
can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring
cycle in its decimal fraction part.
"""

from decimal import getcontext, Decimal

def cycle_length(d):
    getcontext().prec = 2*d+20
    r = str(Decimal(1) / Decimal(d))[10:]
    if len(r) < d:
        return 0
    for l in range(1,d):
        if r[:l] != r[l:2*l]:
            continue
        if r[:d] != r[l:d+l]:
            continue
        return l
    assert False

def solution():
    #return max((cycle_length(d), d) for d in range(2,1000))[1]
    # cycle of 1/d can't exceed d-1 so bail out early:
    best_length, best_d = 0, 0
    for d in range(999,1,-1):
        if d < best_length:
            return best_d
        length = cycle_length(d)
        if length > best_length:
            best_length, best_d = length, d
