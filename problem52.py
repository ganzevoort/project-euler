"""
It can be seen that the number, 125874, and its double, 251748, contain
exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.
"""


import itertools


# pretty fast (255ms) for a first approach
# but not satisfying
def solution1():
    for x in itertools.count(1):
        # assumes no digit duplication
        if all(set(str(x))==set(str(n*x)) for n in [2,3,4,5,6]):
            return x


# now this is damn fast!
# but cheating
def solution2():
    x = 142857
    #print [n*x for n in [2,3,4,5,6]]
    return x


# try harder
def solution():
    # for 6*x to have the same number of digits (d),
    # let base = 10^(d-1)
    # 6*x < 10*base, so x in [1.0..1.67]*base.
    # first digit is 1, second digit in [0..6]
    # 2x in [2.0..3.34]*base    so we have a digit 2 or 3
    # 3x in [3.0..4.99]*base    so we have a 3 or 4
    # 4x in [4.0..6.67]*base    so we have a 4, 5 or 6
    # 5x in [5.0..8.34]*base    so we have a 5, 6, 7 or 8
    # 6x in [6.0..9.99]*base    so we have a 6, 7, 8 or 9
    # if 1.00 <= x/base < 1.20 then
    #   2x starts with a 2
    #   3x starts with a 3
    #   4x starts with a 4
    #   5x starts with a 5
    #   6x starts with a 6 or 7
    # if 1.20 <= x/base < 1.25 then
    #   2x starts with a 2
    #   3x starts with a 3
    #   4x starts with a 4
    #   5x starts with a 6
    #   6x starts with a 7
    # if 1.25 <= x/base < 1.34 then
    #   2x starts with a 2
    #   3x starts with a 3
    #   4x starts with a 5
    #   5x starts with a 6
    #   6x starts with a 7
    # if 1.34 <= x/base < 1.50 then
    #   2x starts with a 2
    #   3x starts with a 4
    #   4x starts with a 5
    #   5x starts with a 6 or 7
    #   6x starts with a 8
    # if 1.50 <= x/base < 1.67 then
    #   2x starts with a 3
    #   3x starts with a 4
    #   4x starts with a 6
    #   5x starts with a 7 or 8
    #   6x starts with a 9
    # concluding: value x should start with 1 and then include all digits
    # from one of the # following sequences:
    sequences = [
        "23456", "23457", "23467", "23567", "24568", "24578", "34679", "34689"
    ]
    # assuming that a solution exists that doesn't need other digits or
    # duplication.
    solutions = set()
    for sequence in sequences:
        for permutation in itertools.permutations(sequence):
            # first digit 1, second digit in [0..6]
            if permutation[0] > '6':
                continue
            x = int(''.join(('1',) + permutation))
            if all(set(str(x))==set(str(n*x)) for n in [2,3,4,5,6]):
                solutions.add(x)
    return sorted(solutions)[0]


