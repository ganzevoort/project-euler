"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text
file containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each
name, multiply this value by its alphabetical position in the list to
obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN,
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the
list. So, COLIN would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?
"""


def name_value(name, index):
    return sum(ord(c)-ord('A')+1 for c in name) * index

def name_list(filename):
    return sorted(name.strip('"').upper()
                  for name in open(filename).read().split(','))


def solution():
    return sum(name_value(name, i+1)
               for i, name in enumerate(name_list('names.txt')))


if __name__ == '__main__':
    N = 938
    name = name_list('names.txt')[N-1]
    print(name, name_value(name, N))

