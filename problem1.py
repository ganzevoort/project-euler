"""
If we list all the natural numbers below 10 that are multiples of
3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def solution1(N=1000):
    return sum(n for n in range(1,N) if n%3==0 or n%5==0)


# solution above is O(N).
# For N=1000, this is fast enough.
# For N=10M, it exceeds 1s runtime.
# it can be O(1).

import math

def sum_below(n):
    # sum(range(n)) == n * (n-1) // 2
    return n * (n-1) // 2

def solution2(N = 1000):
    # sum of all multiples of x below N == x * sum(range(N/x))
    # add multiples of 3 and multiples of 5 but substract multiples of 15
    # as otherwise they'd be counted twice
    return (
        3 * sum_below(math.ceil(N/3)) +
        5 * sum_below(math.ceil(N/5)) -
        15 * sum_below(math.ceil(N/15)))


solution = solution2


if __name__ == '__main__':
    import time
    for solution in solution1, solution2:
        N = '1'
        start = time.time()
        while len(N) < 30:
            result = solution(int(N))
            print("{}ms N={} {}={}".format(
                    int((time.time() - start)*1000),
                    N, solution.__name__, result))
            if time.time() - start > 1.0:
                break
            N += '0'
