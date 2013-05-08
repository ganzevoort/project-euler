"""
The nth term of the sequence of triangle numbers is given by, tn =
n(n+1)/2; so the first ten triangle numbers are:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For
example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word
value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text
file containing nearly two-thousand common English words, how many are
triangle words?
"""


import math


def is_triangle(t):
    # n * (n+1) / 2 = t
    # quadratic equation: n^2 + n - 2t = 0  (a=1, b=1, c=-2t)
    # n = (-b +/- math.sqrt(b^2 - 4ac)) / 2a
    n = (-1 + math.sqrt(1 + 8*t)) / 2
    return n == int(n)

def word_value(word):
    return sum(ord(c)-ord('A')+1 for c in word)

def is_triangle_word(word):
    return is_triangle(word_value(word))

def solution():
    words = [word.strip('"') for word in open('words.txt').read().split(',')]
    return len(filter(is_triangle_word, words))

#print is_triangle(word_value('SKY'))
