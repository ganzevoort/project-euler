"""
Pentagonal numbers are generated by the formula, Pn=n(3n-1)/2. The first
ten pentagonal numbers are:

    1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their
difference, 70  22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and
difference are pentagonal and D = |Pk - Pj| is minimised; what is the
value of D?
"""


import itertools
import math
from gmpy import is_square


def pentagonal(n):
    return n * (3*n-1) // 2

def is_pentagonal(p):
    # p == n * (3*n-1) / 2, p in N, n in N, p>0, n>0
    # quadratic equation  ax^2 + bx + c = 0  ->  x = (-b +- sqrt(b^2-4ac)) / 2a
    # 3*n^2 - n - 2p == 0
    # a=3, b=-1, c=-2p  -> n = (1 + sqrt(1+24p)) / 6
    n = (1 + math.sqrt(1+24*p)) / 6
    return n==int(n)


"""
    P(a+b) = P(a) + P(b) + 3*a*b
    P(a-b) = P(a) + P(b) - 3*a*b + b
    --
    P(a) + P(b) = P(a+b) - 3*a*b
    P(k) = P(d) + P(j) = P(d+j) - 3*d*j
    P(k) + P(j) = P(d+j) - 3*d*j + P(j)
                = P(d+2*j) - 3*(2*d+j)*j
    --
    P(d) = (3*d^2 - d) / 2
    P(j) = (3*j^2 - j) / 2
    P(k) = P(j) + P(d)               = (3*d^2 - d + 3*j^2 - j) / 2
    P(s) = P(k)+P(j) = 2*P(j) + P(d) = (3*d^2 - d + 6*j^2 - 2*j) / 2
    --
    3*k^2 - k = 3*d^2 - d + 3*j^2 - j
    3*s^2 - s = 3*d^2 - d + 6*j^2 - 2*j
    --
    P(d+2*j) = P(d+j) + P(j) + 3*(d+j)*j
    --
    P(d) + P(j) = P(k), P(k) + P(j) = P(n), P(d) + 2*P(j) = P(n)
    P(k) = P(d) + P(j) = P(d+j) - 3*j*d
    P(n) = P(j) + P(k) = P(j) + P(d+j) - 3*j*d
                       = P(d+2*j) - 3*(d+j)*j - 3*j*d
    --
    is_P(P(k)) = is_P(P(d) + P(j))
        = is_P( (3*d^2-d + 3*j^2-j) / 2 )
        = is_int( (1 + math.sqrt(1 + 36*d^2-12*d + 36*j^2-12*j)) / 6)
    is_P(P(n)) = is_P(P(d) + 2*P(j))
        = is_P( (3*d^2-d + 6*j^2-2*j) / 2 )
        = is_int( (1 + math.sqrt(1 + 36*d^2-12*d + 72*j^2-24*j)) / 6)
"""

# d = 1912, j = 1020

def solution():  # 1467ms
    for d in itertools.count(1):
        # P(a+b) = P(a) + P(b) + 3*a*b
        # so, P(k+1) = P(k) + P(1) + 3*k*1
        # so, P(k+1)-P(k) = 3*k + 1
        # so, P(k+1)-P(k) > D  ->  3*k+1 > D  ->  k > (D-1)/3
        D = pentagonal(d)
        for j in range(1, d):  #cheat! (D-1)/3
            Pj = pentagonal(j)
            Pk = Pj+D
            if is_pentagonal(Pk) and is_pentagonal(Pj+Pk):
                #print 'd=',d, 'j=',j
                return D

def solution():  # 422ms
    for d in itertools.count(1):
        D_ = 1 + 12*d*(3*d-1)
        for j in range(1, d):  #cheat! (D-1)/3
            J_ = 12*j*(3*j-1)
            K_ = D_ + J_
            if not is_square(K_):
                continue
            N_ = K_ + J_
            if not is_square(N_):
                continue
            k_ = int(math.sqrt(K_))
            if k_ % 6 != 5:
                continue
            n_ = int(math.sqrt(N_))
            if n_ % 6 != 5:
                continue
            #print 'd=',d, 'j=',j
            return pentagonal(d)

