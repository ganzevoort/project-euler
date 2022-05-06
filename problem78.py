"""
https://projecteuler.net/problem=78

Coin partitions

Problem 78
Let p(n) represent the number of different ways in which n coins
can be separated into piles. For example, five coins can be separated
into piles in exactly seven different ways, so p(5)=7.

    OOOOO
    OOOO O
    OOO OO
    OOO O O
    OO OO O
    OO O O O
    O O O O O

Find the least value of n for which p(n) is divisible by one million.
"""


import time
import itertools
import functools


# s1    0.000s        0ms N=1 ways=1
# s1    0.000s        0ms N=2 ways=2
# s1    0.000s        0ms N=3 ways=3
# s1    0.000s        0ms N=4 ways=5
# s1    0.000s        0ms N=5 ways=7
# s1    0.000s        0ms N=6 ways=11
# s1    0.000s        0ms N=7 ways=15
# s1    0.000s        0ms N=8 ways=22
# s1    0.000s        0ms N=9 ways=30
# s1    0.000s        0ms N=10 ways=42
# s1    0.000s        0ms N=11 ways=56
# s1    0.000s        0ms N=12 ways=77
# s1    0.001s        0ms N=13 ways=101
# s1    0.001s        0ms N=14 ways=135
# s1    0.001s        0ms N=15 ways=176
# s1    0.001s        0ms N=16 ways=231
# s1    0.001s        0ms N=17 ways=297
# s1    0.001s        0ms N=18 ways=385
# s1    0.001s        0ms N=19 ways=490
# ...
# s1  285.508s      405ms
#                   N=2000 ways=4720819175619413888601432406799959512200344166
# memory usage at that moment: 274MB, CPU usage >98%
def solution1(divisible_by=1_000_000, verbose=False, timeout=None):
    """
    write N as a sum a0 + a1 + ... an
    with n > 0, 0 < a0 <= N, 0 < ai <= a(i-1)
    recursion: pass in limit too:
    """
    @functools.lru_cache(maxsize=1_000_000_000)
    def ways(N, limit):
        if N == 0:
            return 1
        return sum(
            ways(N-a0, min(N-a0, a0))
            for a0 in range(1, limit+1)
        )

    t0 = time.time()
    for n in itertools.count(1):
        t1 = time.time()
        result = ways(n, n)
        if isinstance(verbose, int) and verbose > 1:
            print("s1 {:8.3f}s {:8}ms N={} ways={}".format(
                (time.time()-t0),
                int(1000*(time.time()-t1)),
                n, result))
        if result % divisible_by == 0:
            break
        if timeout and time.time()-t0 > timeout:
            break
    if verbose:
        print("s1 {:8}ms N={} ways={}".format(
            int(1000*(time.time()-t0)),
            n, result))
    return n


"""
    N=1 ways=1
    N=2 ways=2
    N=3 ways=3
    N=4 ways=5
    N=5 ways=7
    N=6 ways=11
    N=7 ways=15
    N=8 ways=22
    N=9 ways=30

    calculate p(6)=11:
        first pick 1, 5 remaining, then one option:
            O O O O O O
        first pick 2, 4 remaining, 3 options:
            OO OO OO
            OO OO O O
            OO O O O O
            invalid:
                OO OOOO
                OO OOO O
        first pick 3, 3 remaining, 3 options:
            OOO OOO
            OOO OO O
            OOO O O O
        first pick 4: 2 remaining, 2 options:
            OOOO OO
            OOOO O O
        first pick 5: 1 remaining: 1 option:
            OOOOO O
        first pick 6: 0 remaining: 1 option:
            OOOOOO

    calculate p(n):
        first pick 1, n-1 remaining, then one option:
            O O O O O O
        first pick k, 1 < k < n/2, n-k remaining, ?? options:
            invalid:
                OO OOOO
                OO OOO O
            valid:
                OO OO OO
                OO OO O O
                OO O O O O
            = p(n-k) - ???
        first pick k, n/2 <= k <= n, n-k remaining, p(n-k) options:
            OOO OOO
            OOO OO O
            OOO O O O
        first pick 4: 2 remaining, 2 options, matches above:
            OOOO OO
            OOOO O O
        first pick 5: 1 remaining: 1 option, matches above:
            OOOOO O
        first pick 6: 0 remaining: 1 option, matches above:
            OOOOOO
        p(n) = A + B where
        A = sum(... for k in range(1, (n+1)//2))
        B = sum(p(n-k) for k in range((n+1)//2, n+1))
        with k' = n-k: B = sum(p(k') for k' in range(0, n//2+1))

    calculate p(7)=15:
        first pick 1, 6 remaining, then one option:
            O O O O O O O
        first pick 2, 5 remaining, ? options:   p(n-k) - ???
            invalid:
                OO OOOOO
                OO OOOO O
                OO OOO OO
                OO OOO O O
            valid:
                OO OO OO O
                OO OO O O O
                OO O O O O O
        first pick 3, 4 remaining, 4 options:       p(n-k) - ???
            invalid:
                OOO OOOO
            valid:
                OOO OOO O
                OOO OO OO
                OOO OO O O
                OOO O O O O
        first pick 4: 3 remaining, 3 options:       p(n-k)
        first pick 5: 2 remaining: 2 option:        p(n-k)
        first pick 6: 1 remaining: 1 option:        p(n-k)
        first pick 7: 0 remaining: 1 option:        p(n-k)
"""


"""
See https://en.wikipedia.org/wiki/Partition_(number_theory)

Restricted part size or number of parts
---------------------------------------
By taking conjugates, the number pk(n) of partitions of n into
exactly k parts is equal to the number of partitions of n in which
the largest part has size k. The function pk(n) satisfies the
recurrence

    p(k,n) = p(k, n−k) + p(k−1, n−1)

with initial values p(0, 0) = 1 and p(k, n) = 0 if n ≤ 0 or k ≤ 0 and
n and k are not both zero.[13]

One recovers the function p(n) by
    p(n) = sum(p(k, n) for k in range(0, n+1))

"""
def solution2(divisible_by=1_000_000, verbose=False, timeout=None):
    @functools.lru_cache(maxsize=1_000_000_000)
    def p(k, n):
        if k == n == 0:
            return 1
        elif k <= 0 or n <= 0:
            return 0
        else:
            return p(k, n-k) + p(k-1, n-1)
    @functools.lru_cache(maxsize=1_000_000_000)
    def ways(n):
        return sum(p(k, n) for k in range(0, n+1))

    t0 = time.time()
    for n in itertools.count(1):
        t1 = time.time()
        result = ways(n)
        if isinstance(verbose, int) and verbose > 1:
            print("s2 {:8.3f}s {:8}ms N={} ways={}".format(
                (time.time()-t0),
                int(1000*(time.time()-t1)),
                n, result))
        if result % divisible_by == 0:
            break
        if timeout and time.time()-t0 > timeout:
            break
    if verbose:
        print("s2 {:8}ms N={} ways={}".format(
            int(1000*(time.time()-t0)),
            n, result))
    return n


"""
Partition function

... by Euler's pentagonal number theorem this function is an alternating sum
of pentagonal number powers of its argument.

    p(n) = p(n-1) + p(n-2) - p(n-5) - p(n-7) + ...  if n>= 0 else 0

Pentagonal numbers are (see problem 44) k*(3*k-1)//2

[(f(k), f(-k), '+' if k%2 else '-') for k in range(1,5)]
>>> [(1, 2, '+'), (5, 7, '-'), (12, 15, '+'), (22, 26, '-')]
"""
def solution3(divisible_by=1_000_000, verbose=False, timeout=None):
    p = [1]
    @functools.lru_cache(maxsize=1_000_000_000)
    def ways(n):
        f = lambda k: k*(3*k-1)//2
        if n < 0:
            return 0
        assert(len(p) == n)
        result = 0
        for k in itertools.count(1):
            sign = +1 if k%2 else -1
            for i in (f(k), f(-k)):
                if i > n:
                    p.append(result)
                    return result
                result += sign * p[n-i]

    t0 = time.time()
    for n in itertools.count(1):
        t1 = time.time()
        result = ways(n)
        if isinstance(verbose, int) and verbose > 1:
            print("s3 {:8.3f}s {:8}ms N={} ways={}".format(
                (time.time()-t0),
                int(1000*(time.time()-t1)),
                n, result))
        if result % divisible_by == 0:
            break
        if timeout and time.time()-t0 > timeout:
            break
    if verbose:
        print("s3 {:8}ms N={} ways={}".format(
            int(1000*(time.time()-t0)),
            n, result))
    return n


solution = solution3


if __name__ == '__main__':
    solutions = (solution1, solution2, solution3)
    for solution in solutions:
        solution(verbose=3, divisible_by=627)
    for solution in solutions:
        solution(verbose=True, timeout=10)
