import sys
import itertools

if __name__=='__main__':
    import time
    args = sys.argv[1:] or ("problem{}".format(n) for n in itertools.count(1))
    for arg in args:
        try:
            problem = __import__(arg, globals())
        except ImportError:
            break
        print "%12s" % arg,
        start = time.time()
        result = problem.solution()
        end = time.time()
        print '%-32s %6dms' % (result, 1000*(end-start))

