"""
Convergents of e

See https://projecteuler.net/problem=65 for full description because
copying formatting here is too complicated.

The square root of 2 can be written as an infinite continued fraction.

               1
    √2 = 1 + ---------------
                   1
             2 + -----------
                       1
                 2 + -------
                     2 + ...

The infinite continued fraction can be written, √2 = [1;(2)], (2)
indicates that 2 repeats ad infinitum. In a similar way,
√23 = [4;(1,3,1,8)].

It turns out that the sequence of partial values of continued
fractions for square roots provide the best rational approximations.
Let us consider the convergents for √2.

                    1       3
                1 + -    =  -
                    2       2

                  1         7
            1 + -----    =  -
                    1       5
                2 + -
                    2

              1             17
        1 + ---------    =  --
                 1          12
            2 + -----
                    1
                2 + -
                    2

          1                 41
    1 + -------------    =  --
              1             29
        2 + ---------
                 1
            2 + -----
                    1
                2 + -
                    2

Hence the sequence of the first ten convergents for √2 are:
       3  7  17  41  99  239  577  1393  3363
    1, -, -, --, --, --, ---, ---, ----, ----, ...
       2  5  12  29  70  169  408   985  2378

What is most surprising is that the important mathematical constant,
    e = [2;1,2,1,1,4,1,1,6,1,...,1,2k,1,...].

The first ten terms in the sequence of convergents for e are:
          8  11  19  87  106  193  1264  1457
    2, 3, -, --, --, --, ---, ---, ----, ----, ...
          3   4   7  32   39   71   465   536

The sum of digits in the numerator of the 10th convergent is 1+4+5+7 = 17.

Find the sum of digits in the numerator of the 100th convergent of
the continued fraction for e.
"""



"""
    √2 = [1;(2)]
    e = [2;1,2,1,1,4,1,1,6,1,...,1,2k,1,...].

Approximations:
    1.  a0

    2.        1      a0*a1 + 1
        a0 + --   =  ---------
             a1         a1

    3.          1
        a0 + -------  =  ... gets complicated
                   1
             a1 + --
                  a2

Define:

    xkk     ak
    ---  =  --
    ykk      1

    xjk            1
    ---  =  aj + --------------  =
    yjk                    1
                 a(j+1) + -----
                          ...
                             ak

                    1
            aj + ---------  =
                  x(j+1)k
                  -------
                  y(j+1)k

                  y(j+1)k
            aj + ---------  =
                  x(j+1)k

            x(j+1)k * aj + y(j+1)k
            ----------------------
                  x(j+1)k

    The nth approximation is x0(n-1) / y0(n-1)
"""


from fractions import Fraction


def cf_sqrt2(i):                #   √2 = [1;(2)]
     return 1 if i==0 else 2

def cf_e(i):                    #   e = [2;1,2,1,1,4,1,1,6,1,...,1,2k,1,...].
     return 2 if i==0 else 1 if i%3 != 2 else 2*(i//3 + 1)


class Approximator:
    def __init__(self, cf):
        self.cf = cf

    def nth(self, N):
        k = N-1
        (x, y) = (self.cf(k), 1)
        for j in range(k-1, -1, -1):
            (x, y) = (x * self.cf(j) + y, x)
        return Fraction(x,y)


def solution(N=100):
    """
    Find the sum of digits in the numerator of the 100th convergent
    of the continued fraction for e.
    """
    approximator = Approximator(cf_e)
    numerator = approximator.nth(N=N).numerator
    return sum(int(digit) for digit in str(numerator))


if __name__ == '__main__':
    for cf in cf_sqrt2, cf_e:
        print(cf.__name__, [cf(i) for i in range(20)])
        approximator = Approximator(cf)
        for N in range(1,11):
            print(f"{N}: {approximator.nth(N)}")
    print(f"solution(N=10): {solution(N=10)}")
    print(f"solution(N=100): {solution(N=100)}")
