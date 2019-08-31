"""
Maximum path sum II

By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.

               3
              7 4
             2 4 6
            8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right
click and 'Save Link/Target As...'), a 15K text file containing a
triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is
not possible to try every route to solve this problem, as there are
299 altogether! If you could check one trillion (1012) routes every
second it would take over twenty billion years to check them all.
There is an efficient algorithm to solve it. ;o)


"""


from problem18 import solution as solution_18


def solution():
    return solution_18(grid_text=open('p067_triangle.txt').read())
    grid = list(filter(len,
            [list(map(int,line.split())) for line in grid_text.split('\n')]))

    for y in reversed(range(len(grid)-1)):
        for x in range(len(grid[y])):
            grid[y][x] += max(grid[y+1][x], grid[y+1][x+1])
    return grid[0][0]


if __name__ == '__main__':
    print(solution())