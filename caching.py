"""
Implement caching, e.g.

    @CachingDecorator
    def is_catprime(p, q):
        strp, strq = str(p), str(q)
        return is_prime(int(strp + strq)) and is_prime(int(strq + strp))
    is_catprime.cache_hashkey = mul

For testing purposes, the decorated function has methods cache_reset() and cache_show()
The decorated function may have its cache_hashkey() method replaced.
"""


import time
import json


class Profiler:
    def __init__(self):
        self.calls = 0
        self.time = 0.0

    def __bool__(self):
        return bool(self.calls and self.time)

    def __add__(self, other):
        new = Profiler()
        new.calls = self.calls + other.calls
        new.time = self.time + other.time
        return new

    def call(self, time):
        self.calls += 1
        self.time += time

    def show(self, total=None):
        if total:
            call_pct = "({:5.1f}%)".format(100 * self.calls / total.calls)
            time_pct = "({:5.1f}%)".format(100 * self.time / total.time)
        else:
            call_pct = ""
            time_pct = ""
        output = "{:8} {:8} in {:7.3f}s {:8}".format(
                    self.calls, call_pct,
                    self.time, time_pct)
        if self.calls:
            output += " {:7.3f}ms/call".format(1000 * self.time / self.calls)
        return output


class CachingDecorator:
    def __init__(self, function):
        self.function = function
        self.cache_reset()

    def cache_reset(self):
        self.history = {}
        self.hits = Profiler()
        self.miss = Profiler()

    def cache_show(self):
        if self.history:
            print("cache size: {}".format(len(self.history)))
            total = self.hits + self.miss
            print("hits ", self.hits.show(total=total))
            print("miss ", self.miss.show(total=total))
            print("total", total.show())

    def cache_hashkey(self, *args, **kwargs):
        return json.dumps((args, kwargs))

    def __call__(self, *args, **kwargs):
        t0 = time.time()
        hashkey = self.cache_hashkey(*args, **kwargs)
        try:
            result = self.history[hashkey]
            self.hits.call(time.time() - t0)
        except KeyError:
            is_hit = 'miss'
            result = self.function(*args, **kwargs)
            self.history[hashkey] = result
            self.miss.call(time.time() - t0)
        return result
