"""
Starting in the top left corner of a 2x2 grid, and only being able to
move to the right and down, there are exactly 6 routes to the bottom
right corner.


How many such routes are there through a 20x20 grid?
"""

def fac(n):
    fac = 1
    for i in range(2, n+1):
        fac *= i
    return fac

def solution():
    w, h = 20, 20
    return fac(w+h) // (fac(w)*fac(h))
