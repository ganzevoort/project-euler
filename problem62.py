"""

The cube, 41063625 (345^3), can be permuted to produce two other cubes:
56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest
cube which has exactly three permutations of its digits which are
also cube.

Find the smallest cube for which exactly five permutations of its digits
are cube.

"""


import time
import itertools
from collections import defaultdict


class CubeFactory(object):
    def __init__(self):
        self.cube_list = []
        self.cube_set = set()
        self.horizon = 0

    def fetch_one(self):
        n = len(self.cube_list) + 1
        c = n*n*n
        self.cube_list.append(c)
        self.cube_set.add(c)
        self.horizon = c
        return c

    def is_cube(self, c):
        while c > self.horizon:
            self.fetch_one()
        return c in self.cube_set

    def get_cubes(self):
        for n in itertools.count(1):
            if n <= len(self.cube_list):
                yield self.cube_list[n-1]
            else:
                yield self.fetch_one()


if True:
    _factory = CubeFactory()
    get_cubes = _factory.get_cubes
    is_cube = _factory.is_cube

else:
    def get_cubes():
        for n in itertools.count(1):
            yield n*n*n
    def is_cube(c):
        n = int(round(c**(1.0/3)))
        return n*n*n == c


def solution1(verbose=False, N=5):
    start = time.time()
    t0 = int(start)
    seen = {}
    for i, cube in enumerate(get_cubes()):
        pcubes = list(filter(
                lambda p: p>cube and is_cube(p),
                set(map(
                    lambda p: int(''.join(p)),
                    itertools.permutations(str(cube))
                    ))))
        if len(pcubes) not in seen:
            seen[len(pcubes)] = True
            if verbose:
                print("{}ms: {}".format(
                        int(1000*(time.time()-start)),
                        sorted([cube] + pcubes)))
        if verbose and time.time()-t0 >= 10.0:
            t0 = int(time.time())
            print("{}ms: {}^3 = {}".format(
                    int(1000*(time.time()-start)),
                    i+1, cube))
        if len(pcubes)+1 == N:
            return cube

# After 5 minutes:
# 0ms: [1]
# 0ms: [125, 512]
# 3924ms: [41063625, 56623104, 66430125]
# 9850ms: 476^3 = 107850176
# 19868ms: 519^3 = 139798359
# 29981ms: 562^3 = 177504328
# 39841ms: 604^3 = 220348864
# 49806ms: 645^3 = 268336125
# 59764ms: 687^3 = 324242703
# 69699ms: 729^3 = 387420489
# 79798ms: 772^3 = 460099648
# 89847ms: 815^3 = 541343375
# 99780ms: 858^3 = 631628712
# 109797ms: 901^3 = 731432701
# 119907ms: 944^3 = 841232384
# 129971ms: 983^3 = 949862087
# 140486ms: [1006012008, 1061208000, 8012006001, 8120601000]
# 140486ms: 1002^3 = 1006012008
# 151982ms: 1007^3 = 1021147343
# 163933ms: 1012^3 = 1036433728
# 174463ms: 1016^3 = 1048772096
# 184716ms: 1020^3 = 1061208000
# 197352ms: 1025^3 = 1076890625
# 208369ms: 1029^3 = 1089547389
# 217979ms: 1033^3 = 1102302937
# 229454ms: 1038^3 = 1118386872
# 241265ms: 1043^3 = 1134626507
# 250721ms: 1047^3 = 1147730823
# 263491ms: 1052^3 = 1164252608
# 273280ms: 1056^3 = 1177583616
# 282707ms: 1060^3 = 1191016000
# 294859ms: 1065^3 = 1207949625
# 307163ms: 1070^3 = 1225043000
# 317213ms: 1074^3 = 1238833224
# 326925ms: 1078^3 = 1252726552
# 339137ms: 1083^3 = 1270238787

# Each time the resulting cube has an extra digit, the process speed
# slows, time needed per cube is O(digits!).  There is no hope for
# a result today.
# The number of permutations grows really fast:
# >>> len(list(itertools.permutations(str(1006012008))))
# 3628800


# Instead of checking all permutations to see if they're cube,
# we'll check all cubes to see if they're permutations.
# This delivers in 60ms!
# Even N=16 is under 1 second.

from pprint import pprint
def find_permutations(cubeset, N):
    # sort cubeset in bins
    bins = defaultdict(list)
    for cube in cubeset:
        bins[''.join(sorted(str(cube)))].append(cube)
    return [
        sorted(permutations)
        for pip, permutations in bins.items()
        if len(permutations)==N
    ]

def solution2(verbose=False, N=5):
    if verbose:
        print("N={}".format(N))
    start = time.time()
    t0 = int(start)
    current_length = 0
    cubeset = []
    for i, cube in enumerate(get_cubes()):
        cube_length = len(str(cube))
        if cube_length > current_length:
            results = find_permutations(cubeset, N)
            if results:
                if verbose:
                    print("{}ms:".format(
                            int(1000*(time.time()-start))))
                    for result in results:
                        print("\t{}".format(result))
                return min(min(results))
            cubeset = []
            current_length = cube_length
            if verbose:
                print("{}ms: {}^3 = {} (length {})".format(
                        int(1000*(time.time()-start)),
                        i+1, cube, cube_length))
        cubeset.append(cube)


solution = solution2

if __name__=='__main__':
    print(solution2(verbose=True, N=1))
    print(solution2(verbose=True, N=2))
    print(solution2(verbose=True, N=3))
    print(solution2(verbose=True, N=4))
    print(solution2(verbose=True, N=5))
    print(solution2(verbose=True, N=6))
    print(solution2(verbose=True, N=16))
