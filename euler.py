# See http://projecteuler.net for problems,
# http://code.google.com/p/projecteuler-solutions/ for solutions


import sys
import itertools


if __name__=='__main__':
    solutions = dict(('problem'+line.strip().replace(' ','')).split('.',1)
                     for line in file('solutions.txt')
                     if not line.startswith('#'))
    import time
    args = sys.argv[1:] or ("problem{}".format(n) for n in itertools.count(1))
    for arg in args:
        try:
            problem = __import__(arg, globals())
        except ImportError:
            break
        print "%12s" % arg,
        start = time.time()
        result = str(problem.solution())
        end = time.time()
        status = 'OK' if result==solutions.get(arg) else 'WRONG'
        print '%-6s%-32s %6dms' % (status, result, 1000*(end-start))

