"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two
primes and concatenating them in any order the result will always be
prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The
sum of these four primes, 792, represents the lowest sum for a set of
four primes with this property.

Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime.
"""


import sys
import time
from functools import reduce
from operator import mul
from collections import defaultdict
from collections import namedtuple
from itertools import combinations
from primes import get_primes
from miller_rabin import is_prime


# This is an exercise in optimization.
#
# First, we make sure to do as little work as possible especially
# for bigger prime numbers.  We keep a list of candidate sets pet
# length. For each prime, we try to grow each candidate sets by
# adding that prime to the candidate, checking for the catprime
# criterium. If we already have a result, candidate sets that cannot
# be grown to a better result are dropped.
#
# Second, we recognise that the catprime test is called very, very
# often (almost 9 million times), and often with same parameters
# (93% of the time) so we add caching to the is_catprime() function.
# Also, miller_rabin.is_prime beats primes.is_prime on this problem
# even then, about 55% of the time is spent in is_prime() alone!
#
# The result of this is solution1(). It's not totally unreadable.
#
# Then the fun started.
# We separated phase1 (before a result is found) from phase2 (after)
# because these phases require different optimizations.
# In phase1, it makes sense to pre-calculate cat_twins, the set of
# all primes q where q < p and q, p are catprimes. This avoids all
# calls to is_catprime. It's not needed to sort the candidate lists
# until a first result is found. After that, we make sure the lists
# remain sorted.
# In phase2, is_catprime is inlined (see cat_seen, cat_twins sets)
# to reduce the overhead of the functioncall (adds up to 0.8s).
#
# The result of this is solution2(). It's about 4 times in lines
# of code, and much more complex. Unless speed is absolutely really
# really really more important than anything else, I'd use solution1.


_history = dict()
def is_catprime(p, q):
    hashed = p*q
    try:
        result = _history[hashed]
        return result
    except KeyError:
        strp, strq = str(p), str(q)
        result = is_prime(int(strp + strq)) and is_prime(int(strq + strp))
        _history[hashed] = result
        return result


CPSet = namedtuple('CPSet', ['sum', 'primes'])


def solution1(verbose=False, N=5):
    # About 22s
    start = time.time()
    candidates = defaultdict(list)
    candidates[0] = [CPSet(sum=0, primes=())]
    bestsum = None
    for p in get_primes():
        for length in range(N-1,-1,-1):
            candidates[length].sort()
            for i, S in enumerate(candidates[length]):
                if bestsum and S.sum + (N-length) * p >= bestsum:
                    del candidates[length][i:]
                    break
                elif all(is_catprime(p, q) for q in S.primes):
                    newset = CPSet(sum=S.sum + p, primes=S.primes + (p,))
                    if length==N-1:
                        bestsum = newset.sum
                        if verbose:
                            print("{}, {}".format(
                                "%.3fs" % (time.time()-start), newset))
                    else:
                        candidates[length+1].append(newset)
        if bestsum and not candidates[N-1]:
            return bestsum


def solution2(verbose=False, N=5):
    # About 15s
    start = time.time()
    candidates = defaultdict(list)
    bestsum = None
    seenprimes = []
    for p in get_primes():
        if p in [2,5]:
            continue

        if not bestsum:
            # first phase, still looking for a match.
            # About 12.4s
            strp = str(p)
            cat_twins = set()
            for q in seenprimes:
                strq = str(q)
                if is_prime(int(strp + strq)) and is_prime(int(strq + strp)):
                    cat_twins.add(q)
            if not cat_twins:
                seenprimes.append(p)
                continue
            for length in range(N-1,1,-1):
                for S in candidates[length]:
                    if bestsum and S.sum + (N-length) * p >= bestsum:
                        continue
                    elif not (set(S.primes) - cat_twins):
                        newset = CPSet(sum=S.sum + p, primes=S.primes + (p,))
                        if length==N-1:
                            bestsum = newset.sum
                            if verbose:
                                print("{}, {}".format(
                                    "%.3fs" % (time.time()-start), newset))
                        else:
                            candidates[length+1].append(newset)
            for q in cat_twins:
                candidates[2].append(CPSet(sum=p+q, primes=(q, p)))
            if bestsum:
                # End of phase1, next up phase2, we found one.
                # sort the lists so we can quickly remove all
                # candidates that have no prospect of growing to a
                # better solution.
                for length in range(N-1,2,-1):
                    candidates[length].sort()

        else:
            # second phase, looking for a better match.
            # About 2.1s
            new = defaultdict(list)
            # inlining the is_catprime() functionality here, including
            # history, brings phase2 down from 2.9s to 2.1s
            cat_seen = set()
            cat_twins = set()  # incomplete
            strp = str(p)
            for length in range(N-1,1,-1):
                for i, S in enumerate(candidates[length]):
                    if S.sum + (N-length) * p >= bestsum:
                        del candidates[length][i:]
                        break

                    # can_extend = all(is_catprime(p, q) for q in S.primes)
                    can_extend = True
                    for q in S.primes:
                        if q not in cat_seen:
                            cat_seen.add(q)
                            strq = str(q)
                            if (is_prime(int(strp + strq)) and
                                    is_prime(int(strq + strp))):
                                cat_twins.add(q)
                            else:
                                can_extend = False
                                break
                        elif q not in cat_twins:
                            can_extend = False
                            break

                    if can_extend:
                        newset = CPSet(sum=S.sum + p, primes=S.primes + (p,))
                        if length==N-1:
                            bestsum = newset.sum
                            if verbose:
                                print("{}, {}".format(
                                        "%.3fs" % (time.time()-start), newset))
                        else:
                            new[length+1].append(newset)
            for q in seenprimes:
                if q+(N-1)*p >= bestsum:
                    break
                if is_catprime(p, q):
                    new[2].append(CPSet(sum=p+q, primes=(q, p)))
            for length in range(N-1,1,-1):
                if new[length]:
                    candidates[length].extend(new[length])
                    candidates[length].sort()
            if not any (candidates[length] for length in range(2,N)):
                return bestsum

        seenprimes.append(p)


solution = solution2

if __name__=='__main__':
    try:
        N = int(sys.argv[1])
    except (IndexError, ValueError):
        N = 4
    verbose = True
    for solution in solution2, solution1:
        _history = dict()
        start = time.time()
        print("{}(N={}, verbose={})".format(solution.__name__, N, verbose))
        result = solution(N=N, verbose=verbose)
        totaltime = time.time() - start
        print("{} => {}".format("%.3fs" % totaltime, result))
        print()
