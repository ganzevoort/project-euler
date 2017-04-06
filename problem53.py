"""
There are exactly ten ways of selecting three from five, 12345:

    123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, C(5,3) = 10.

In general,

C(n,r) = ( n! ) / ( r! * (n-r)! )
where r <= n, n! = n*(n-1)!, 0! = 1.

It is not until n = 23, that a value exceeds one-million: C(23,10) = 1144066.

How many, not necessarily distinct, values of C(n,r), for 1 <= n <= 100,
are greater than one-million?
"""


class Factorials(object):
    def __init__(self, N):
        # precalculate all factorial numbers up to 100!
        self.value = [1] * (N+1)
        fac = 1
        for i in range(1, N+1):
            fac *= i
            self.value[i] = fac

    def C(self, n, r):
        return self.value[n] / (self.value[r] * self.value[n-r])


def solution1(N=100, M=1000000):
    f = Factorials(N)
    biggies = 0
    for n in range(1,101):
        for r in range(0, N):
            if f.C(n,r) > M:
                biggies += 1
                #print n,r,f.C(n,r)
    return biggies

def solution2(N=100, M=1000000):
    f = Factorials(N)
    biggies = 0
    for n in range(1,101):
        # C(n,r) == C(n, n-r), so symmetrical
        for r in range(0, (N+1)/2):
            if f.C(n,r) > M:
                # also: C(n,r') > M for all r' where r <= r' <= (n-r)
                biggies += (n-r) - r + 1
                break
    return biggies

solution = solution2
