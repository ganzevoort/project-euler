"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""


def solution(N=1000):
    return sum(map(int,str(pow(2,N))))


if __name__ == '__main__':
    for N in 15, 1000:
        print("{}: {}".format(N, solution(N)))
