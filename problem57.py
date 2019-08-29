# -*- coding: utf-8 -*-
"""
It is possible to show that the square root of two can be expressed as
an infinite continued fraction.

    √ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

    1 + 1/2 = 3/2 = 1.5
    1 + 1/(2 + 1/2) = 7/5 = 1.4
    1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
    1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth
expansion, 1393/985, is the first example where the number of digits in
the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a
numerator with more digits than denominator?
"""


from fractions import Fraction


# Using fractions module; 332ms
def solution1(N=1000, verbose=False):
    n_gt_d = 0
    f = Fraction(1)
    for i in range(N):
        f = Fraction(1) + Fraction(1) / (f + 1)
        if len(str(f.numerator)) != len(str(f.denominator)):
            n_gt_d += 1
        if verbose:
            print("%4d %s %f" % (i+1, f, f))
    return n_gt_d


# now using num/den notation: 3ms
def solution2(N=1000, verbose=False):
    n_gt_d = 0
    (num, den) = (1, 1)
    for i in range(N):
        (num, den) = (num + 2 * den, num + den)
        if len(str(num)) != len(str(den)):
            n_gt_d += 1
        if verbose:
            print("%4d %d/%d %f" % (i+1, num, den, float(num)/den))
    return n_gt_d


# Crazy fast, avoid log10(x) or len(str(x)): 0ms :D
def solution3(N=1000, verbose=False):
    n_gt_d = 0
    (num, den) = (1, 1)
    # to avoid len(str(x)) calculations, we keep tenpowers for num, den:
    (tpn, tpd) = (10, 10)
    # so: num < tpn, den < tpd
    for i in range(N):
        (num, den) = (num + 2 * den, num + den)
        if num >= tpn:
            tpn *= 10
        if den >= tpd:
            tpd *= 10
        if tpn != tpd:
            n_gt_d += 1
        if verbose:
            print("%4d %d/%d %f" % (i+1, num, den, float(num)/den))
    return n_gt_d


solution = solution3


if __name__=='__main__':
    print(solution(N=10, verbose=True))

    def compare_times(N=1000):
        import time
        for f in solution3, solution2, solution1:
            start = time.time()
            result = f(N=N)
            duration = time.time() - start
            print('%-6s%-32s %6dms' % (result, f.__name__, 1000*duration))

    compare_times()
    #  153  solution3                             0ms
    #  153  solution2                             3ms
    #  153  solution1                           332ms
    compare_times(N=10000) # N=1K was too fast to measure, now try with N=10K
    # 1508  solution3                            15ms
    # 1508  solution2                          1777ms
    # 1508  solution1                        147368ms

