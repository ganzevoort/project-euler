"""
The 5-digit number, 16807=7^5, is also a fifth power. Similarly,
the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?

"""


import itertools


def solution(verbose=False):
    # 10^n is an (n+1)-digit number, so for each n-digit positive
    # integer that is an n-th power x^n, x should be < 10.
    # if 9^n is a less-than-n-digit number, 9^n' for n'>n will also
    # be a less-than-n'-digit number.
    results = 0
    for n in itertools.count(1):
        for x in range(1,10):
            if len(str(pow(x,n)))==n:
                results += 1
                if verbose:
                    print("{}^{}={}".format(x,n,pow(x,n)))
        if len(str(pow(9,n))) < n:
            # no more results after this
            return results


if __name__ == '__main__':
    print(solution(verbose=True))
