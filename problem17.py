"""
If the numbers 1 to 5 are written out in words: one, two, three,
four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in
total.

If all the numbers from 1 to 1000 (one thousand) inclusive were
written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred
and forty-two) contains 23 letters and 115 (one hundred and fifteen)
contains 20 letters. The use of "and" when writing out numbers is
in compliance with British usage.
"""


words = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
}


def say(n):
    thousands = n // 1000
    hundreds = (n % 1000) // 100
    n %= 100

    in_letters = ""
    if thousands:
        in_letters +=  words[thousands] + "thousand"
    if hundreds:
        in_letters +=  words[hundreds] + "hundred"
    if not n:
        return in_letters
    elif in_letters:
        in_letters +=  "and"

    if n not in words:
        words[n] = words[10*(n//10)] + words[n%10]

    in_letters +=  words[n]
    return in_letters


def solution(N=1000):
    return sum(len(say(i)) for i in range(1,N+1))


if __name__ == '__main__':
    for i in range(1,1001):
        print(say(i))
