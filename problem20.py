"""
n! means n * (n - 1) * ... * 3 * 2 * 1

For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""


def fac(n):
    fac = 1
    for i in range(2, n+1):
        fac *= i
    return fac


def solution(N=100):
    return sum(map(int,str(fac(N))))


if __name__ == '__main__':
    for N in (10, 100):
        print('{}! = {}'.format(N, fac(N)))
        print('sum of digits: {}'.format(solution(N)))
