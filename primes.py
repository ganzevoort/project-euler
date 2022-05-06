import itertools
import math
import pyprimesieve


class PrimeFactory(object):
    def __init__(self):
        pass

    @staticmethod
    # Paul Hofstra, http://code.activestate.com/recipes/117119/
    def erat2a():
        D = {}
        yield 2
        for q in itertools.islice(itertools.count(3), 0, None, 2):
            p = D.pop(q, None)
            if p is None:
                D[q * q] = 2 * q # use here 2 * q
                yield q
            else:
                x = p + q
                while x in D:
                    x += p
                D[x] = p

    def is_prime(self, q):
        for p in self.erat2a():
            if p*p > q:
                return True
            elif q % p == 0:
                return False
        return True

    def get_primes(self, N=None):
        for p in self.erat2a():
            if N and p > N:
                return
            yield p


class PrimeFactory2(PrimeFactory):
    def __init__(self):
        self.prime_list = []
        self.prime_set = set()
        self.horizon = 0
        self.fetcher = self.erat2a()

    def fetch_one(self):
        p = next(self.fetcher)
        self.prime_list.append(p)
        self.prime_set.add(p)
        self.horizon = p
        return p

    def get_primes(self, N=None):
        n, p = 0, 0
        while True:
            if p < self.horizon:
                p = self.prime_list[n]
            else:
                p = self.fetch_one()
            if N and p > N:
                return
            yield p
            n += 1

    def is_prime(self, q):
        if q in self.prime_set:
            return True
        elif q < self.horizon:
            return False
        return all(q % p != 0 for p in self.get_primes(int(math.sqrt(q))))


class PrimeFactory3(PrimeFactory2):
    def is_prime(self, q):
        if q <= self.horizon:
            return q in self.prime_set
        elif q <= 3 * self.horizon:
            while self.horizon < q:
                self.fetch_one()
            return q in self.prime_set
        return all(q % p != 0 for p in self.get_primes(int(math.sqrt(q))))


class PrimeFactory4(PrimeFactory2):
    def prefetch(self, N):
        while self.horizon < N:
            self.fetch_one()

    def is_prime(self, q):
        if q in self.prime_set:
            return True
        if q < self.horizon:
            return False
        for p in self.prime_list:
            if q % p == 0:
                return False
            if p * p > q:
                return True
        while True:
            self.fetch_one()
            p = self.horizon
            if q % p == 0:
                return False
            if p * p > q:
                return True


class PrimeFactory5(PrimeFactory):
    def __init__(self):
        self.prime_list = []
        self.prime_set = set()
        self.horizon = 0

    def fetch_one(self):
        p = pyprimesieve.primes_nth(len(self.prime_list)+1)
        self.prime_list.append(p)
        self.prime_set.add(p)
        self.horizon = p
        return p

    def prefetch(self, N):
        if N > self.horizon*2:
            self.prime_list = pyprimesieve.primes(N)
            self.prime_set = set(self.prime_list)
            self.horizon = N
            return
        while self.horizon < N:
            self.fetch_one()

    def get_primes(self, N=None):
        if N is None:
            start_index = 0
            while True:
                end_index = len(self.prime_list)
                for p in self.prime_list[start_index:end_index]:
                    yield p
                start_index = end_index
                self.prefetch(max(self.horizon * 3, 3))
        self.prefetch(N)
        for p in self.prime_list:
            if p >= N:
                return
            yield p

    def is_prime(self, q):
        if q in self.prime_set:
            return True
        if q < self.horizon:
            return False
        for p in self.prime_list:
            if q % p == 0:
                return False
            if p * p > q:
                return True
        self.prefetch(max(int(math.sqrt(q))+1, self.horizon*3))
        for p in self.prime_list:
            if q % p == 0:
                return False
            if p * p > q:
                return True


_factory = PrimeFactory5()
is_prime = _factory.is_prime
get_primes = _factory.get_primes
prefetch_primes = _factory.prefetch


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return x * y // gcd(x,y)


def prime_divisors(n):
    for factor, power in pyprimesieve.factorize(n):
        for _ in range(power):
            yield factor

def divisors(n):
    divisors = set([1])
    for p in prime_divisors(n):
        divisors.update([p*d for d in divisors])
    return sorted(divisors)


if __name__=='__main__':
    import time
    start = time.time()
    N = 1000000
    S = 37550402023
    assert S == sum(get_primes(N))
    assert S == sum(filter(is_prime, range(2,N+1)))
    end = time.time()
    print('%5dms' % (1000*(end-start)))

