"""
https://projecteuler.net/problem=68


Consider the following "magic" 3-gon ring, filled with the numbers
1 to 6, and each line adding to nine.

                4
                 \
                  3
                 / \
                1 - 2 - 6
               /
              5

Working clockwise, and starting from the group of three with the
numerically lowest external node (4,3,2 in this example), each
solution can be described uniquely. For example, the above solution
can be described by the set: 4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9,
10, 11, and 12. There are eight solutions in total.

    Total   Solution Set
       9      4,2,3; 5,3,1; 6,1,2
       9      4,3,2; 6,2,1; 5,1,3
      10      2,3,5; 4,5,1; 6,1,3
      10      2,5,3; 6,3,1; 4,1,5
      11      1,4,6; 3,6,2; 5,2,4
      11      1,6,4; 5,4,2; 3,2,6
      12      1,5,6; 2,6,4; 3,4,5
      12      1,6,5; 3,5,4; 2,4,6

By concatenating each group it is possible to form 9-digit strings;
the maximum string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is
possible to form 16- and 17-digit strings. What is the maximum
16-digit string for a "magic" 5-gon ring?


                O
                  \
                    O     O
                  /   \  /
                O       O
              /  \     /
            O     O - O - O
                   \
                    O

"""


# Take a permutation of [1,2,3,..,10]. If number 10 is in one of
# the center nodes, it will occur 2x in the resultstring making it
# a 17-digit string. Therefore, number 10 should be on an external
# node.


import time
import itertools


class MagicRing:
    def __init__(self, N, permutation):
        # first half represents external nodes, second half represents
        # center nodes.
        # Connected nodes, for 1<=x<=N: p[x], p[N+x], p[N+(x+1)%N]
        self.N = N
        self.permutation = permutation

    def solutionset(self):
        N = self.N
        p = self.permutation
        return [
                [p[x], p[N+x], p[N+(x+1)%N]]
                for x in range(N)
        ]

    def ismagic(self):
        solutionset = self.solutionset()
        expected = sum(solutionset[0])
        return all(sum(x)==expected for x in solutionset)

    def stringvalue(self):
        try:
            return self._stringvalue
        except AttributeError:
            self._stringvalue = int(''.join(
                    str(cell)
                    for group in self.solutionset()
                    for cell in group))
            return self._stringvalue


def best_rings(N):
    # Low numbers should be on the center nodes.
    # Startnumber should be lowest high number
    low_numbers = list(range(1,N+1))
    high_numbers = list(range(N+1,2*N+1))
    startnumber = high_numbers.pop(0)
    for firsthalf in itertools.permutations(high_numbers):
        for secondhalf in itertools.permutations(low_numbers):
            ring = MagicRing(N, (startnumber,) + firsthalf + secondhalf)
            if ring.ismagic():
                yield ring


def solution(N=5, verbose=False):
    t0 = time.time()
    result = None
    for ring in best_rings(N):
        if verbose:
            print(ring.solutionset(), ring.stringvalue())
        if not result or result < ring.stringvalue():
            result = ring.stringvalue()
    t1 = time.time()
    if verbose:
        print("{}ms - result: {}".format(int(1000*(t1-t0)), result))
    return result


if __name__ == '__main__':
    solution(N=3, verbose=True)
    solution(N=5, verbose=True)
