"""
If p is the perimeter of a right angle triangle with integral length
sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p < 1000, is the number of solutions maximised?
"""


import math


def solution():
    N = 1000
    s = {}
    # a < b < c
    # a + b + c = p < 1000
    # a^2 + b^2 = c^2
    for a in range(1,N):
        for b in range(a+1,N):
            cf = math.sqrt(a*a + b*b)
            c = int(cf)
            p = a+b+c
            if p >= N:
                break
            elif c==cf:
                s.setdefault(p,[]).append((a,b,c))
    #from pprint import pprint ; pprint(s)
    return max((len(v),k) for k,v in s.items())[1]

