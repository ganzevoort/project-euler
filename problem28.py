"""
Starting with the number 1 and moving to the right in a clockwise
direction a 5 by 5 spiral is formed as follows:

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
formed in the same way?
"""


def s1():
    N = 1001
    n = 1
    sum = 1
    for ring in range(2,N,2):
        for corner in 'se', 'sw', 'ne', 'nw':
            n += ring
            sum += n
        assert(n == (ring+1)*(ring+1))
    return sum

def s2():
    N = 1001
    return 1+sum(4*i*i + 10*i + 10 for i in range(1,N-1,2))

def s3():
    N = 1001
    return (1 +
            sum(4*i*i for i in range(1,N-1,2)) +
            sum(10*i for i in range(1,N-1,2)) +
            sum(10 for i in range(1,N-1,2)))

def s4():
    N = 1001
    return (1 +
            4*sum(i*i for i in range(1,N-1,2)) +
            5*((N-1)*(N-3)/2) +
            10*N-10 )

if __name__=='__main__':
    import time
    result1 = s1()
    for s in s1, s2, s3, s4:
        print s.__name__,
        start = time.time()
        import time
        result = s()
        end = time.time()
        print '%-32s %6dms' % (result, 1000*(end-start))
        assert result==result1

solution = s4

