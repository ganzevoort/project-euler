# See http://projecteuler.net for problems,
# http://code.google.com/p/projecteuler-solutions/ for solutions


import sys
import itertools


def get_problems():
    for n in itertools.count(1):
        yield "problem{}".format(n)


if __name__=='__main__':
    solutions = dict(('problem'+line.strip().replace(' ','')).split('.',1)
                     for line in open('solutions.txt').readlines()
                     if not line.startswith('#'))
    total_duration = 0.0
    max_duration = 0.0
    import time
    args = []
    for arg in sys.argv[1:] or get_problems():
        try:
            problem = __import__(arg, globals())
            args.append(arg)
        except ImportError:
            break
        print("%12s " % arg, end='')
        start = time.time()
        result = str(problem.solution())
        duration = time.time() - start
        total_duration += duration
        max_duration = max(max_duration, duration)

        status = 'OK' if result==solutions.get(arg) else 'WRONG'
        print('%-6s%-32s %6dms' % (status, result, 1000*duration))
    if len(args) > 1:
        print("%12s " % 'total', end='')
        print('%-6s%-32s %6dms' % ('', '', 1000*total_duration))
        print("%12s " % 'avg', end='')
        print('%-6s%-32s %6dms' % ('', '', 1000*total_duration/len(args)))
        print("%12s " % 'max', end='')
        print('%-6s%-32s %6dms' % ('', '', 1000*max_duration))

