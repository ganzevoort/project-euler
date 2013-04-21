"""
The Fibonacci sequence is defined by the recurrence relation:
    Fn = F(n-1) + F(n-2), where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?
"""

def fibonacci():
    i0, i1 = 1, 1
    while True:
        yield i0
        i0, i1 = i1, i0 + i1

def solution():
    for i, fi in enumerate(fibonacci()):
        if len(str(fi)) >= 1000:
            return i+1

