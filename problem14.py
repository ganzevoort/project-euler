"""
The following iterative sequence is defined for the set of positive integers:

    n -> n/2 (n is even)
    n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13  40  20  10  5  16  8  4  2  1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def collatz_sequence(n):
    cs = [n]
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        cs.append(n)
    return cs

csl = {}
def collatz_sequence_length(n):
    if n == 1:
        return 1
    elif n in csl:
        return csl[n]
    elif n % 2 == 0:
        length = 1 + collatz_sequence_length(n / 2)
    else:
        length = 1 + collatz_sequence_length(3 * n + 1)
    csl[n] = length
    return length

def solution():
    N = 1000000
    return max((collatz_sequence_length(n), n) for n in range(1,N))[1]
