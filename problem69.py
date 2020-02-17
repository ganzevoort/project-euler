"""
https://projecteuler.net/problem=69

Totient maximum

Problem 69
Euler's Totient function, φ(n) [sometimes called the phi function],
is used to determine the number of numbers less than n which are
relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are
all less than nine and relatively prime to nine, φ(9)=6.

     n  | Relatively Prime  | φ(n)  | n/φ(n)
    ----+-------------------+-------+----------
     2  | 1                 | 1     | 2
     3  | 1,2               | 2     | 1.5
     4  | 1,3               | 2     | 2
     5  | 1,2,3,4           | 4     | 1.25
     6  | 1,5               | 2     | 3
     7  | 1,2,3,4,5,6       | 6     | 1.1666...
     8  | 1,3,5,7           | 4     | 2
     9  | 1,2,4,5,7,8       | 6     | 1.5
    10  | 1,3,7,9           | 4     | 2.5

It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
"""


import time
from primes import get_primes, gcd


def is_relative_prime(p, q):
    return gcd(p, q) == 1

def relative_primes(n):
    return [p for p in range(1,n) if is_relative_prime(p, n)]

def phi(n):
    return len(relative_primes(n))


def print_table(N=10):
    tableformat = "{:2} | {:16} | {:4} | {}"
    print(tableformat.format(
        "n", "Relatively Prime", "φ(n)", "n/φ(n)"))
    for n in range(2,11):
        rplist = ",".join(str(p) for p in relative_primes(n))
        print(tableformat.format(
            n, rplist, phi(n), n/phi(n)))


def solution1(N=1000000):
    # solution1(N=10): 6  -- 0ms
    # solution1(N=100): 30  -- 2ms
    # solution1(N=1000): 210  -- 335ms
    # solution1(N=10000): 2310  -- 39367ms
    # ... N=100K expected in 1 hour, N=1M expected in 4 days :(
    return max(range(2, N+1), key=lambda n: n/phi(n))


# This quite literally implements the problem as stated, but appears
# to be O(N^2). Not surprisingly, because we have nested loops.
# Even if we can calcultate phi(n) in O(1), the resulting solution
# will be O(N), which is more than we'd like.
# For a fast solution for large N, it's not possible to calculate
# n/phi(n) for each n <= N, so we have to look more into what it
# means.
# I have a strong suspition that n/phi(n) is high if n is as non-prime
# as possible.  Multiplying primes will have that effect.
#     2*3 = 6, 2*3*5 = 30, 2*3*5*7 = 210 etc.
# This leads to the correct answer, but can we prove this to be
# correct?
def solution2(N=1000000):
    # solution2(N=10): 6  -- 0ms
    # solution2(N=100): 30  -- 0ms
    # solution2(N=1000): 210  -- 0ms
    # solution2(N=10000): 2310  -- 0ms
    # solution2(N=100000): 30030  -- 0ms
    # solution2(N=1000000): 510510  -- 0ms
    n = 1
    for p in get_primes():
        result = n
        n = n*p
        if n > N:
            return result


solution = solution2


if __name__ == '__main__':
    print("relative_primes(9): {}".format(relative_primes(9)))
    print_table()
    for solution in solution2, solution1:
        for N in 10, 100, 1000, 10000, 100000, 1000000:
            t0 = time.time()
            result = solution(N=N)
            t1 = time.time()
            print("{}(N={}): {}  -- {}ms".format(
                solution.__name__, N, result, int(1000*(t1-t0))))
