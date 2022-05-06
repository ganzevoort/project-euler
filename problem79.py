"""
https://projecteuler.net/problem=79

Passcode derivation

Problem 79
A common security method used for online banking is to ask the user
for three random characters from a passcode. For example, if the
passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters;
the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order,
analyse the file so as to determine the shortest possible secret
passcode of unknown length.
"""


import time
import itertools
from collections import defaultdict


"""
By hand:
    129
    129 + 160 = 12960
    129 + 160 + 162 = 16290
    129 + 160 + 162 + 168 = 162908
    129 + 160 + 162 + 168 + 180 = 162980
    129 + 160 + 162 + 168 + 180 + 289 + 290 = 162890
    129 + 160 + 162 + 168 + 180 + 289 + 290 + 316 + 318 + 319 + 362 +
          368 + 380 + 389 + 620 + 629 + 680 + 689 + 690 
          = 3162890
    129 + 160 + 162 + 168 + 180 + 289 + 290 + 316 + 318 + 319 + 362 +
          368 + 380 + 389 + 620 + 629 + 680 + 689 + 690 + 710 + 716 +
          718 + 719 + 720 + 728 + 729 + 731 + 736 + 760 + 769 + 790 +
          890
          = 73162890
"""
def solution_byhand(verbose=False):
    result = 73162890
    if verbose:
        print("s1 {:8}ms result={}".format(
            int(1000*(time.time()-t0)),
            result))
    return result



def solution(verbose=False):
    """
    If keylog contains abc, then (some) a should be before b, before c.
    for each digit, keep a list of digits we want before it.
    After scanning all entries, take the first digit to be the one with
    shortest before list (what if not empty?), emit it and take it out of
    the before list of the other digits. Repeat till done. 
    """
    t0 = time.time()
    # duplicates don't add value, and order of attempts has no meaning
    keylog = sorted(set(
        line.strip()
        for line in open('keylog.txt').readlines()
    ))
    before = {digit: set() for digit in set(''.join(keylog))}
    for attempt in keylog:
        for a, b in itertools.combinations(attempt, 2):
            before[b].add(a)
    result = ''
    while before:
        # take digit with shortest before list
        digit = min(before.keys(), key=lambda k: len(before[k]))
        if isinstance(verbose, int) and verbose > 1:
            print(
                    "s1 {:8}ms\n"
                    "\tresult:\t{}\n"
                    "\tbefore:\t{}\n"
                    "\tchoose:\t{}".format(
                        int(1000*(time.time()-t0)),
                        result,
                        "\n\t\t".join(
                            "{}: [{}]".format(d, ''.join(sorted(s)))
                            for d, s in sorted(before.items())
                        ),
                        digit))
        if before[digit]:
            # Dependency cycle, emit the before digits too. This leads to
            # a valid result but I'm not 100% sure it's optimal
            result += ''.join(sorted(before[digit]))
            for s in before.values():
                for d in s.intersection(set(result)):
                    s.remove(d)
        # emit
        result += digit
        # take it out of the before list of the other digits
        for s in before.values():
            if digit in s:
                s.remove(digit)
        del before[digit]
    if verbose:
        print("s1 {:8}ms result={}".format(
            int(1000*(time.time()-t0)),
            result))
    return int(result)


if __name__ == '__main__':
    solution(verbose=2)
