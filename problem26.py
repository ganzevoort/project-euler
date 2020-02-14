"""
A unit fraction contains 1 in the numerator. The decimal representation
of the unit fractions with denominators 2 to 10 are given:

    1/2 =   0.5
    1/3 =   0.(3)
    1/4 =   0.25
    1/5 =   0.2
    1/6 =   0.1(6)
    1/7 =   0.(142857)
    1/8 =   0.125
    1/9 =   0.(1)
    1/10    =   0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It
can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring
cycle in its decimal fraction part.
"""


#from decimal import getcontext, Decimal

def cycle_length(d, verbose=False):
    #   77 / 1 \ 0.(012987)
    #         0
    #        -- -
    #        10
    #         77
    #        --- -
    #         23
    #         154
    #         --- -
    #          76
    #          693
    #          --- -
    #           67
    #           616
    #           --- -
    #            54
    #            539
    #            --- -
    #              1
    digits = ''
    n = 1
    seen = []
    while n != 0:
        seen.append(n)
        n *= 10
        x = n // d
        n -= x*d
        digits += str(x)
        if n in seen:
            length = len(seen) - seen.index(n)
            if verbose:
                print(f"1/{d}: 0.{digits[:len(digits)-length]}({digits[-length:]})  -- {length}")
            return length
    if verbose:
        print(f"1/{d}: 0.{digits}")
    return 0


def solution(N=1000, verbose=False):
    # return max(range(2,N), key=cycle_length)
    # cycle of 1/d can't exceed d-1 so bail out early:
    best_length, best_d = 0, 0
    for d in range(999,1,-1):
        if d <= best_length:
            return best_d
        length = cycle_length(d, verbose=verbose)
        if length > best_length:
            best_length, best_d = length, d


if __name__ == '__main__':
    for d in range(2,11):
        cycle_length(d,verbose=True)
    print()
    print(solution(verbose=True))
