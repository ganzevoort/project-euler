"""
https://projecteuler.net/problem=81

Path sum: two ways

Problem 81
In the 5 by 5 matrix below, the minimal path sum from the top left
to the bottom right, by only moving to the right and down, is
indicated in bold red and is equal to 2427.

       >131  673  234  103   18
       >201 > 96 >342  965  150
        630  803 >746 >422  111
        537  699  497 >121  956
        805  732  524 > 37 >331

Find the minimal path sum from the top left to the bottom right by
only moving right and down in matrix.txt, a 31K text file containing
an 80 by 80 matrix.
"""


import math


SAMPLEMATRIX = [
    [131, 673, 234, 103, 18],
    [201, 96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524, 37, 331],
]


def minimal_path_sum(matrix, verbose=False):
    height = len(matrix)
    width = max(len(row) for row in matrix)
    if verbose:
        print(f"matrix size {width}x{height}")
    """
	For each position in the matrix, we'll annotate what the
	minimal path sum is to reach that position.
    We can approach this top-to-bottom, left-to-right. For each position
    [x,y], the minimal path is either through [x-1,y] or [x,y-1].
    """
    minimal_sums = [
        [0 for column in range(width)]
        for row in range(height)
    ]
    for x in range(width):
        for y in range(height):
            previous = []
            if x > 0:
                previous.append(minimal_sums[y][x-1])
            if y > 0:
                previous.append(minimal_sums[y-1][x])
            if previous:
                minimal_sums[y][x] = min(previous) + matrix[y][x]
            else:
                minimal_sums[y][x] = matrix[y][x]
    result = minimal_sums[height-1][width-1]
    if verbose > 1:
        print("matrix:")
        from pprint import pprint; pprint(minimal_sums)
    if verbose:
        print(f"result {result}")
    return result


def read_matrix(filename):
    lines = open(filename).readlines()
    return [list(map(int, line.strip().split(','))) for line in lines]


def solution(verbose=False):
    return minimal_path_sum(read_matrix('p081_matrix.txt'), verbose=verbose)


if __name__ == '__main__':
    assert minimal_path_sum(SAMPLEMATRIX, verbose=2) == 2427
    solution(verbose=True)
