"""
Diophantine equation

Problem 66
Consider quadratic Diophantine equations of the form:

        x^2 – Dy^2 = 1

For example, when D=13, the minimal solution in x is
        649^2 – 13×180^2 = 1.

It can be assumed that there are no solutions in positive integers
when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain
the following:

        3^2 – 2×2^2 = 1
        2^2 – 3×1^2 = 1
        9^2 – 5×4^2 = 1
        5^2 – 6×2^2 = 1
        8^2 – 7×3^2 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest
x is obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the
largest value of x is obtained.
"""


import math
from gmpy import is_square
import itertools
from collections import namedtuple
import time


Solution = namedtuple('Solution', ['x', 'y', 'D'])

def solution(N=1000, verbose=False):
    start = time.time()
    bestD = 0
    bestx = 0
    for D in range(N+1):
        t0 = time.time()
        s = minimal_diophantine_equation_solution(D)
        if s and s.x > bestx:
            if verbose:
                print(f"{int((time.time()-t0)*1000)}ms: {s}")
            bestx, bestD = s.x, D
    if verbose:
        print(f"{int((time.time()-start)*1000)}ms: best D: {bestD}")
    return bestD


def minimal_diophantine_equation_solution(D):
    if is_square(D):
        return None

    attempt = 2

    if attempt == 1:
        for x in itertools.count(2):
            if x % 10000000 == 0:
                y = int(math.sqrt((x*x - 1.0) / D))
                print("D={}, x={}M, y~{}M".format(
                    D, x//1000000, y//1000000))
            if (x*x - 1) % D == 0 and is_square((x*x - 1) // D):
                y = int(math.sqrt((x*x - 1.0) / D))
                return Solution(x, y, D)
    # usually, this is pretty fast (< 1ms), but:
    # 1ms: Solution(x=9801, y=1820, D=29)
    # 3ms: Solution(x=24335, y=3588, D=46)
    # 12ms: Solution(x=66249, y=9100, D=53)
    # 2ms: Solution(x=19603, y=2574, D=58)
    # Solution(x=?, y=?, D=61) takes forever (x > 1000M)

    # minimal x means minimal (x^2 - 1) / D means minimal y
    # loop over y:
    elif attempt == 2:
        for y in itertools.count(1):
            x_square = D*y*y + 1
            if y % 10000000 == 0:
                x = int(math.sqrt(x_square))
                print("D={}, x~{}M, y={}M".format(
                    D, x//1000000, y//1000000))
            if is_square(x_square):
                x = int(math.sqrt(x_square))
                return Solution(x, y, D)
    # faster, but ot fast enough
    # 1ms: Solution(x=24335, y=3588, D=46)
    # 3ms: Solution(x=66249, y=9100, D=53)
    # 80511ms: Solution(x=1766319049, y=226153980, D=61)


"""
Think harder about these Diophantine equations:

    x^2 – Dy^2 = 1

    d = √D

          x^2 + 1
    d^2 = -------
            y^2

    x / y is an approximation of √D
"""

from problem64 import ContinuedFraction
from problem65 import Approximator


class SquareRootApproximator(ContinuedFraction, Approximator):
    def __init__(self, D):
        self.D = D
        self.cf = self.a
        super().__init__(D)

    def a(self, i):
        if i==0:
            return self.a0
        period = len(self.repeating)
        return self.repeating[(i-1) % period]


def minimal_diophantine_equation_solution(D, verbose=False):
    if is_square(D):
        return None

    sqa = SquareRootApproximator(D)
    for N in itertools.count(1):
        f = sqa.nth(N)
        if verbose:
            print(f"{N}: {f}")
        (x, y) = (f.numerator, f.denominator)
        if (x*x - D*y*y == 1):
            return Solution(x, y, D)


if __name__ == '__main__':
    print(minimal_diophantine_equation_solution(D=13, verbose=True))
    print(solution(N=7, verbose=True))
    print(solution(verbose=True))

