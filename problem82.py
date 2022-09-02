"""
https://projecteuler.net/problem=82

Path sum: two ways

Problem 82

NOTE: This problem is a more challenging version of Problem 81.

The minimal path sum in the 5 by 5 matrix below, by starting in any
cell in the left column and finishing in any cell in the right
column, and only moving up, down, and right, is indicated in red
and bold; the sum is equal to 994.

        131  673 >234 >103 > 18
       >201 > 96 >342  965  150
        630  803  746  422  111
        537  699  497  121  956
        805  732  524   37  331

Find the minimal path sum from the left column to the right column
in matrix.txt, a 31K text file containing an 80 by 80 matrix.
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
    For each position [x,y], the minimal path is either through
    [x-1,y] or [x,y-1] or [x,y+1] so we do this slightly different
    than in problem 81.
    """
    minimal_sums = [
        [0 for column in range(width)]
        for row in range(height)
    ]
    for x in range(width):
        # first approach: calculate path as if coming from left
        for y in range(height):
            from_left = minimal_sums[y][x-1] if x > 0 else 0
            minimal_sums[y][x] = from_left + matrix[y][x]
        # see if walking up, or down, improves those paths
        for y in range(height):
            path = minimal_sums[y][x]
            for up in reversed(range(y)):
                path += matrix[up][x]
                if path >= minimal_sums[up][x]:
                    break
                minimal_sums[up][x] = path
            path = minimal_sums[y][x]
            for down in range(y+1, height):
                path += matrix[down][x]
                if path >= minimal_sums[down][x]:
                    break
                minimal_sums[down][x] = path

    result = min(minimal_sums[y][width-1] for y in range(height))
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
    return minimal_path_sum(read_matrix('p082_matrix.txt'), verbose=verbose)


if __name__ == '__main__':
    assert minimal_path_sum(SAMPLEMATRIX, verbose=2) == 994
    solution(verbose=True)
