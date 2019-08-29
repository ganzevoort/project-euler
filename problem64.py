"""
Odd period square roots

See https://projecteuler.net/problem=64 for full description because
copying formatting here is too complicated.


All square roots are periodic when written as continued fractions
and can be written in the form:

                 1
    √N = a0 + ------------------
                      1
              a1 + -------------
                           1
                   a2 + --------
                        a3 + ...

For example, let us consider √23:

    √23 = 4 + √23 - 4

                  1
        = 4 + ---------
                  1
               -------
               √23 - 4

                   1
        = 4 + -----------
                  √23 - 3
              1 + -------
                     7


If we continue we would get the following expansion:

                    1
        √23 = 4 + -------------------
                        1
                  1 + ---------------
                            1
                      3 + -----------
                                1
                          1 + -------
                              8 + ...

The process can be summarised as follows:

    a0 = 4, ...
    a1 = 1, ...
    a2 = 3, ...
    a3 = 1, ...
    a4 = 8, ...
    a5 = 1, ...
    a6 = 3, ...
    a7 = 1, ...

It can be seen that the sequence is repeating. For conciseness, we
use the notation √23 = [4;(1,3,1,8)], to indicate that the block
(1,3,1,8) repeats indefinitely.

The first ten continued fraction representations of (irrational)
square roots are:

    √2  = [1;(2)], period=1
    √3  = [1;(1,2)], period=2
    √5  = [2;(4)], period=1
    √6  = [2;(2,4)], period=2
    √7  = [2;(1,1,1,4)], period=4
    √8  = [2;(1,4)], period=2
    √10 = [3;(6)], period=1
    √11 = [3;(3,6)], period=2
    √12 = [3;(2,6)], period=2
    √13 = [3;(1,1,1,1,6)], period=5

Exactly four continued fractions, for N≤13, have an odd period.

How many continued fractions for N≤10000 have an odd period?

"""


"""
So, I'm confused. Let's look at √23 again:

    √23 = 4 + √23 - 4

Why 4? Probably because 4 is the largest integer < √23.
So: start number a0 = math.floor(math.sqrt(23))

                  1
        = 4 + ---------
                  1
               -------
               √23 - 4

X = 1 / (1 / X). So far so good.

                   1
        = 4 + -----------
                  √23 - 3
              1 + -------
                     7

That's a jump... let's try if we can do that too.
    1 / (√23 - 4) = (√23 + 4) / ((√23 + 4) * (√23 - 4))
                  = (√23 + 4) / (23 - 16)
                  = (√23 + 4) / 7
                  = (7 + √23 - 3) / 7
                  = 1 + (√23 - 3) / 7

    7 / (√23 - 3) = (√23 + 3) * 7 / ((√23 + 3) * (√23 - 3))
                  = (√23 + 3) * 7 / (23 - 9)
                  = (√23 + 3) * 7 / 14
                  = (√23 + 3) / 2
                  = (6 + √23 - 3) / 2
                  = 3 + (√23 - 3) / 2

    2 / (√23 - 3) = (√23 + 3) * 2 / ((√23 + 3) * (√23 - 3))
                  = (√23 + 3) * 2 / (23 - 9)
                  = (√23 + 3) * 2 / 14
                  = (√23 + 3) / 7
                  = (7 + √23 - 4) / 7
                  = 1 + (√23 - 4) / 7

OK...
                                                # N = 23, n = 7, d = 3
    n / (√N - d)  = ((√N + d) * n) / ((√N + d) * (√N - d))
                  = (√N + d) * n / (N - d^2)
                  = (√N + d) * n / k            # k = (N - d^2) = 14
Simplify k' = k / n. Is k always multiple of n? # k' = 2
                  = (√N + d) / k'
Pick a multiple of k': m*k'                     # m = 3
                  = (m*k' + (√N + d - m*k') / k'
                  = m + (√N + d - m*k') / k'
                  = m + (√N - (m*k'-d)) / k'
Which m?
Largest m such that m*k'-d <= a0

    m = math.floor((a0+d)/k')                   # 3/2 < m < 7/2

Right...
"""


import math
from gmpy import is_square


class ContinuedFraction:
    def __init__(self, N, verbose=False):
        self.N = N
        self.verbose = verbose
        self.a0 = math.floor(math.sqrt(N))
        self.repeating = []
        if verbose:
            print(f"init: {self}")
        self.find_repeating()
        if verbose:
            print(f"done: {self}")

    def __str__(self):
        return f"√{self.N} = [{self.a0}; {self.repeating}]"

    def one_step(self, n, d):
        k = self.N-d*d
        k_ = k // n
        m = math.floor((self.a0+d)/k_)
        if self.verbose:
            print(f"one_step: n={n}, d={d}) => k={k}, k'={k_}, m={m}")
        return (m, k_, m*k_-d)

    def find_repeating(self):
        seen = set()
        n = 1
        d = self.a0
        while True:
            (next_a, n, d) = self.one_step(n, d)
            if (n,d) in seen:
                return
            seen.add((n,d))
            self.repeating.append(next_a)


def solution(Nmax=10000, verbose=False):
    odds = 0
    for N in range(Nmax+1):
        if not is_square(N):
            continued_fraction = ContinuedFraction(N)
            if verbose:
                print(continued_fraction)
            if len(continued_fraction.repeating) % 2 == 1:
                odds += 1
    return odds  # what are the odds?


if __name__ == '__main__':
    print(ContinuedFraction(23, verbose=True))
    print(solution(Nmax=13, verbose=True))
