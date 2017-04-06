"""
In the card game poker, a hand consists of five cards and are ranked,
from lowest to highest, in the following way:

    High Card: Highest value card.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    Three of a Kind: Three cards of the same value.
    Straight: All cards are consecutive values.
    Flush: All cards of the same suit.
    Full House: Three of a kind and a pair.
    Four of a Kind: Four cards of the same value.
    Straight Flush: All cards are consecutive values of same suit.
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
    2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the
highest value wins; for example, a pair of eights beats a pair of fives
(see example 1 below). But if two ranks tie, for example, both players
have a pair of queens, then highest cards in each hand are compared
(see example 4 below); if the highest cards tie then the next highest
cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand  | Player 1            | Player 2            | Winner
------+---------------------+---------------------+----------
  1   | 5H 5C 6S 7S KD      | 2C 3S 8S 8D TD      | Player 2
      | Pair of Fives       | Pair of Eights      |
------+---------------------+---------------------+----------
  2   | 5D 8C 9S JS AC      | 2C 5C 7D 8S QH      | Player 1
      | Highest card Ace    | Highest card Queen  |
------+---------------------+---------------------+----------
  3   | 2D 9C AS AH AC      | 3D 6D 7D TD QD      | Player 2
      | Three Aces          | Flush with Diamonds |
------+---------------------+---------------------+----------
  4   | 4D 6S 9H QH QC      | 3D 6D 7H QD QS      | Player 1
      | Pair of Queens      | Pair of Queens      |
      | Highest card Nine   | Highest card Seven  |
------+---------------------+---------------------+----------
  5   | 2H 2D 4C 4D 4S      | 3C 3D 3S 9S 9D      | Player 1
      | Full House          | Full House          |
      | With Three Fours    | with Three Threes   |

The file, poker.txt, contains one-thousand random hands dealt to two
players. Each line of the file contains ten cards (separated by a single
space): the first five are Player 1's cards and the last five are Player
2's cards. You can assume that all hands are valid (no invalid characters
or repeated cards), each player's hand is in no specific order, and in
each hand there is a clear winner.

How many hands does Player 1 win?




Cards, in order: 2 3 4 5 6 7 8 9 T J Q K A
Colors: C H D S  # Note: I use colors where text above uses suits
"""

from collections import defaultdict


values = "AKQJT98765432"
colors = "CHDS"

high_card = 0
one_pair = 1
two_pair = 2
three_of_a_kind = 3
straight = 4
flush = 5
full_house = 6
four_of_a_kind = 7
straight_flush = 8
royal_flush = 9


class Card(object):
    def __init__(self, rep):
        self.rep = rep
        self.value = rep[0]
        self.color = rep[1]

    def __repr__(self):
        return "Card('{}')".format(self.rep)

    def __str__(self):
        return self.rep

    def __cmp__(self, other):
        return cmp(values.index(other.value), values.index(self.value))


class Hand(object):

    def __init__(self, input):
        self.cards = sorted((Card(rep) for rep in input), reverse=True)
        self.ranked = ''

        self.by_value = defaultdict(list)
        self.by_color = defaultdict(list)
        for card in self.cards:
            self.by_value[card.value].append(card.color)
            self.by_color[card.color].append(card.value)
        self.by_length = sorted(
                self.by_value.items(),
                key=lambda (k,v): (len(v), -values.index(k)),
                reverse=True)

        self.ranked = self.rank()


    def __repr__(self):
        return "Hand('{}')".format("','".join(map(str, self.cards)))

    def __str__(self):
        return '{} - {}  '.format(' '.join(map(str, self.cards)), self.ranked)

    def __cmp__(self, other):
        return cmp(self.ranked, other.ranked)

    def is_high_card(self):
        "QC 7D 5H 8C 9S"
        # self.by_length = [('Q', ['C']), ('7', ['D']),
        #                   ('5', ['H']), ('8', ['C']), ('9', ['S'])]
        if len(self.by_length)==5:
            return [v[0] for v in self.by_length]   # ['Q', '9', '8', '7', '5']

    def is_one_pair(self):
        "7C 7D 5H 8C 9S"
        # self.by_length = [('7', ['C', 'D']),
        #                   ('5', ['H']), ('8', ['C']), ('9', ['S'])]
        if len(self.by_length)==4:
            return [v[0] for v in self.by_length]   # ['7', '9', '8', '5']

    def is_two_pair(self):
        "7C 7D 8H 8C 9S"
        # self.by_length = [('7', ['C', 'D']), ('8', ['H', 'C']), ('9', ['S'])]
        if len(self.by_length)==3 and len(self.by_length[0][1])==2:
            return [v[0] for v in self.by_length]   # ['8', '7', '9']

    def is_three_of_a_kind(self):
        "7C 7D 7H 8C 9S"
        # self.by_length = [('7', ['C', 'D', 'H']), ('8', ['C']), ('9', ['S'])]
        if len(self.by_length)==3 and len(self.by_length[0][1])==3:
            return [v[0] for v in self.by_length]   # ['7', '9', '8']

    def is_straight(self):
        "KH QS JH TD 9C"
        keys = [card.value for card in self.cards]
        if len(keys)==5 and ''.join(keys) in values:
            return keys

    def is_flush(self):
        "QH TH 9H 4H 2H"
        if len(self.by_color)==1:
            return self.by_color.values()[0]

    def is_full_house(self):
        "7C 7D 7H 8C 8S"
        # self.by_length = [('7', ['C', 'D', 'H']), ('8', ['C', 'S'])]
        if len(self.by_length)==2 and len(self.by_length[0][1])==3:
            return [v[0] for v in self.by_length]   # ['7', '8']

    def is_four_of_a_kind(self):
        "7C 7D 7H 7S 8S"
        # self.by_length = [('7', ['C', 'D', 'H', 'S']), ('8', ['S'])]
        if len(self.by_length)==2 and len(self.by_length[0][1])==4:
            return [v[0] for v in self.by_length]   # ['7', '8']

    def is_straight_flush(self):
        "KH QH JH TH 9H"
        return self.is_flush() and self.is_straight()

    def is_royal_flush(self):
        "AH KH QH JH TH"
        straight = self.is_straight_flush()
        if straight and 'A' in straight:
            return straight

    def rank(self):
        rank_methods = [
                self.is_high_card,
                self.is_one_pair,
                self.is_two_pair,
                self.is_three_of_a_kind,
                self.is_straight,
                self.is_flush,
                self.is_full_house,
                self.is_four_of_a_kind,
                self.is_straight_flush,
                self.is_royal_flush,
                ]
        # these methods return card values for comparing
        for rank, method in reversed(list(enumerate(rank_methods))):
            is_rank = method()
            if is_rank:
                return (rank, [-values.index(i) for i in is_rank], is_rank)


if __name__=='__main__':
    samples = {}
    for method_name, method in Hand.__dict__.items():
        if method_name.startswith('is_') and method.__doc__:
            samples[method_name] = Hand(method.__doc__.split())
    for method_name, hand in sorted(samples.items(), key=lambda (k,v): v):
        print "%-20s %s" % (method_name, hand)
    import re
    # 1   | 5H 5C 6S 7S KD      | 2C 3S 8S 8D TD      | Player 2
    pattern = re.compile(
            '^\s*(\d+)\s*\|'
            '\s*(\w\w \w\w \w\w \w\w \w\w)\s*\|'
            '\s*(\w\w \w\w \w\w \w\w \w\w)\s*\|'
            '\s*Player (\d+)$')
    for line in __doc__.split('\n'):
        m = pattern.match(line)
        if m:
            print line
            num, p1, p2, winner = m.groups()
            player1 = Hand(p1.split())
            player2 = Hand(p2.split())
            i_say = '1' if player1 > player2 else '2'
            if i_say != winner:
                import pdb; pdb.set_trace()


def hands(filename):
    for line in file(filename):
        cards = line.split()
        yield Hand(cards[:5]), Hand(cards[5:])


def solution():
    wins = 0
    for player1, player2 in hands('p054_poker.txt'):
        if player1 > player2:
            wins += 1
    return wins
