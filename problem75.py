"""
https://projecteuler.net/problem=75

Singular integer right triangles

Problem 75
It turns out that 12 cm is the smallest length of wire that can be
bent to form an integer sided right angle triangle in exactly one
way, but there are many more examples.

    12 cm: (3,4,5)
    24 cm: (6,8,10)
    30 cm: (5,12,13)
    36 cm: (9,12,15)
    40 cm: (8,15,17)
    48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to
form an integer sided right angle triangle, and other lengths allow
more than one solution to be found; for example, using 120 cm it
is possible to form exactly three different integer sided right
angle triangles.

    120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of
L ≤ 1,500,000 can exactly one integer sided right angle triangle
be formed?
"""


import time
import math
import itertools
import functools
import operator
from collections import defaultdict
from pprint import pprint
import pyprimesieve


def solution1(L=1500000, verbose=False):
    t0 = time.time()
    # find all a, b, c
    # where 0 < a < b
    #       a**2 + b**2 = c**2
    #       a + b + c <= L
    triangles = defaultdict(list)
    for a in range(1, L):
        for b in range(a+1, L):
            c = math.floor(math.sqrt(a**2 + b**2))
            if a**2 + b**2 != c**2:
                continue
            if a + b + c <= L:
                if verbose and isinstance(verbose, int) and verbose>1:
                    print(f"{a+b+c}cm: ({a},{b},{c})")
                triangles[a+b+c].append((a,b,c))
    if verbose:
        print("s1 L={} {:8}ms phase1".format(
            L, int(1000*(time.time()-t0))))
    if isinstance(verbose, int) and verbose>1:
        pprint(triangles)
    result = sum(1 for n in triangles.values() if len(n)==1)
    if verbose:
        print("s1 L={} {:8}ms result={}".format(
            L, int(1000*(time.time()-t0)), result))
    return result


def solution2(L=1500000, verbose=False):
    t0 = time.time()
    # Is math.floor(math.sqrt(a**2 + b**2)) expensive?
    # if a + b + c <= L, then c < L/2
    root = { c**2: c for c in range(1, L//2) }
    if verbose:
        print("s2 L={} {:8}ms precalculate roots".format(
            L, int(1000*(time.time()-t0))))
    triangles = defaultdict(list)
    for bsquare, b in root.items():
        if verbose and isinstance(verbose, int) and verbose>2:
            if b%1000 == 0:
                print("s2 L={} {:8}ms b={}".format(
                    L, int(1000*(time.time()-t0)), b))
        for asquare, a in root.items():
            if asquare >= bsquare:
                break
            csquare = asquare + bsquare
            if csquare in root:
                c = root[csquare]
                if a + b + c <= L:
                    if verbose and isinstance(verbose, int) and verbose>1:
                        print(f"{a+b+c}cm: ({a},{b},{c})")
                    triangles[a+b+c].append((a,b,c))
    if verbose:
        print("s2 L={} {:8}ms phase1".format(
            L, int(1000*(time.time()-t0))))
    if isinstance(verbose, int) and verbose>1:
        pprint(triangles)
    result = sum(1 for n in triangles.values() if len(n)==1)
    if verbose:
        print("s2 L={} {:8}ms result={}".format(
            L, int(1000*(time.time()-t0)), result))
    return result


def solution3(L=1500000, verbose=False):
    """
    for positive integers a, b, c where a < b < c and a² + b² = c²:
    let x = b - a, y = c - b
    then a² + (a+x)² = (a+x+y)²
         a² + a² + 2ax + x² = a² + 2a(x+y) + (x+y)²
         a² + a² + 2ax + x² = a² + 2ax + 2ay + x² + 2xy + y²
         a²                 =            2ay +      2xy + y²

    y = 1 => a² = 2a + 2x + 1 => x = (a² - 2a - 1)/2 = a²/2 - a - 1/2
    x is a positive integer, so a is odd, a >= 3

       x |   y |   a |   b |   c
    -----+-----+-----+-----+-----
       1 |   1 |   3 |   4 |   5
       7 |   1 |   5 |  12 |  13
      17 |   1 |   7 |  24 |  25
      31 |   1 |   9 |  40 |  41
      49 |   1 |  11 |  60 |  61

    y = 2 => a² = 4a + 4x + 4 => x = (a² - 4a - 4)/4 = a²/4 - a - 1
    x is a positive integer, so a is even, a >= 6

       x |   y |   a |   b |   c
    -----+-----+-----+-----+-----
       2 |   2 |   6 |   8 |  10
       7 |   2 |   8 |  15 |  17
      14 |   2 |  10 |  24 |  26
      23 |   2 |  12 |  35 |  37
      34 |   2 |  14 |  48 |  50

    y = 3 => a² = 6a + 6x + 9 => x = (a² - 6a - 9)/6 = a²/6 - a - 3/2
    x is a positive integer, so a is odd, multiple of 3, a >= 9

       x |   y |   a |   b |   c
    -----+-----+-----+-----+-----
       3 |   3 |   9 |  12 |  15
      21 |   3 |  15 |  36 |  39
      51 |   3 |  21 |  72 |  75
      93 |   3 |  27 | 120 | 123
     147 |   3 |  33 | 180 | 183

    general case:
    y > 3 => a² = 2ay + 2xy + y² => x = (a² - 2ay - y²) / 2y = a²/(2y) - a - y/2
    if y is odd, a must be odd, a² is a multiple of y
    if y is even, a must be even, a² is a multiple of 2y
    if y is even, 2y = prod(pi yi) for pi prime, yi integer > 0,
    then y' = prod(pi^ceil(yi/2))
    then a² is multiple of y iff a is multiple of y'
    and a2 is multiple of 2y if a is multiple of y' and p0==2, i0 is odd,
    or a is multiple of 2y'

    maximal value of y is if c is large, a and b are close.
    Then y <  (√2 - 1) L / (√2 + 2) < L/8

    x > 0, so a² - 2ay - y² > 0, so a² - 2ay > y²
    quadratic formula:
    ax²+bx+c = 0, then x = (-b±√(b²-4ac))/(2a)
    variable substitution: x:a, a:1, b:-2y, c:-y²
    a²-2ya-y² = 0, then a = (2y±√(4y²+4y²))/2 = y ± y√2
    so, a >= y + y√2
    """

    t0 = time.time()
    triangles = set()
    dups = set()
    for y in range(1, L//8):
        factorized = pyprimesieve.factorize(y)
        y_prime = functools.reduce(
            operator.mul,
            (p**((i+1)//2) for p,i in factorized),
            1
        )
        if y % 2 == 1:
            base = y_prime
            step = y_prime * 2
        else:
            base = y_prime
            if factorized[0][0] == 2 and factorized[0][1] % 2 == 0:
                base *= 2
            step = base
        lwb_a = math.ceil(y*(1+math.sqrt(2)))
        new_base = math.ceil((lwb_a - base) / step) * step + base
        for a in itertools.count(new_base, step):
            x = (a*a - 2*a*y - y*y) // (2*y)
            b = a + x
            c = b + y
            l = a + b + c
            if l > L:
                break
            if isinstance(verbose, int) and verbose>2:
                print(f"s3 L={L}, x={x} y={y} y'={y_prime} ({a},{b},{c}) {a+b+c}cm")
            if l in triangles:
                dups.add(l)
            else:
                triangles.add(l)
    if verbose:
        print("s3 L={} {:8}ms phase1".format(
            L, int(1000*(time.time()-t0))))

    if isinstance(verbose, int) and verbose>1:
        print("triangles: {}\ndups:      {}".format(
            ",".join(map(str, sorted(triangles))),
            ",".join(map(str, sorted(dups)))))
    result = len(triangles) - len(dups)
    if verbose:
        print("s3 L={} {:8}ms result={}".format(
            L, int(1000*(time.time()-t0)), result))
    return result


solution = solution3


if __name__ == '__main__':
    solution1(verbose=3, L=120)
    solution2(verbose=3, L=120)
    solution3(verbose=3, L=120)
    solution2(verbose=True, L=10000)
    solution3(verbose=True, L=10000)
    solution(verbose=True)
