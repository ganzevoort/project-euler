"""
The sum of the squares of the first ten natural numbers is,

    1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first
ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""


def square(x):
    return x * x

def solution1(N=100):
    return (
        square(sum(x for x in range(1,N+1))) -
        sum(square(x) for x in range(1,N+1)))
    return sqsu - susq

# Like problem1, the trivial solution is O(N) but still very fast
# for reasonable values of N
# For N=10M, it exceeds 3s runtime.
#
# The sum of the squares is some 3d-power polynomial
# because the integral of x^2 is 1/3 x^3.
#
# F(N) = sum(x^2 for x in range(1,N+1)) = N^2 + F(N-1)
#
# F(N) = aN^3 + bN^2 + cN + d
# F(0) = 0        >> d=0
#
# (N-1)^2 = N^2-2N+1
# (N-1)^3 = (N-1)(N^2-2N+1) = N^3-2N^2+N - N^2+2N-1 = N^3-3N^2+3N-1
#
# F(N) - F(N-1) - N^2 = 0
#
# (aN^3 + bN^2 + cN) - (a(N-1)^3 + b(N-1)^2 + c(N-1)) - N^2 = 0
# aN^3 + bN^2 + cN - a(N-1)^3 - b(N-1)^2 - cN + c - N^2 = 0
# aN^3 + bN^2 + cN - a(N^3-3N^2+3N-1) - b(N^2-2N+1) - cN + c - N^2 = 0
# aN^3 + bN^2 + cN - aN^3 + 3aN^2 - 3aN + a - bN^2 + 2bN - b - cN + c - N^2 = 0
#
# ( 3a - 1 )*N^2 + ( -3a + 2b )*N + ( a - b + c ) = 0
# # for N=0:
# ( a - b + c ) = 0
# # for N=1:
# ( 3a - 1 + -3a + 2b + a - b + c ) = 0
# ( a + b + c - 1 ) = 0   => (a + b + c - 1) - (a - b + c) = 0
#                         => 2b - 1 = 0
#                         => b = 1/2
#                         => (a + c) = 1/2
# # for N=2:
# ( 12a - 4 + -3a + 2b + a - b + c ) = 0
# ( 10a - 4 + b + c ) = 0 =>
# ( 9a - 4 + 2b ) = 0     => 9a = 3
#                         => a = 1/3
#                         => c = 1/6


def square_of_sums(N):
    return square(N * (N+1) // 2)

def sum_of_squares(N):
    # int((N*N*N / 3 + N*N / 2 + N / 6))
    # This leads to floating point rounding errors for huge N.
    return (N*N*N*2 + N*N*3 + N) // 6

def solution2(N=100):
    return square_of_sums(N) - sum_of_squares(N)


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
