# -*- coding: utf-8 -*-
"""
In England the currency is made up of pound, £, and pence, p, and there
are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

        1x£1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p

How many different ways can £2 be made using any number of coins?
"""

def payment_methods_count(amount, coins):
    coin_value = coins[0][0]
    if amount == 0:
        return 1
    elif len(coins)==1:
        return 1 if (amount % coin_value == 0) else 0
    return sum(payment_methods_count(amount - i*coin_value, coins[1:])
               for i in range(amount/coin_value, -1, -1))

def payment_methods_verbose(amount, coins):
    coin_value = coins[0][0]
    coin_name = coins[0][1]
    if amount == 0:
        yield ""
        return
    elif len(coins)==1:
        if amount % coin_value == 0:
            yield '{}x{}'.format(amount/coin_value, coin_name)
        return
    for i in range(amount/coin_value, 0, -1):
        for m in payment_methods_verbose(amount - i*coin_value, coins[1:]):
            yield "{}x{} {}".format(i, coin_name, m)
    for m in payment_methods_verbose(amount, coins[1:]):
        yield m

def solution():
    coins = [(200, '£2'), (100, '£1'), (50, '50p'), (20, '20p'), 
             (10, '10p'), (5, '5p'), (2, '2p'), (1, '1p')]
    return payment_methods_count(200, coins)
    # faster than:
    return len(list(payment_methods_verbose(200, coins)))

if __name__=='__main__':
    coins = [(200, '£2'), (100, '£1'), (50, '50p'), (20, '20p'), 
             (10, '10p'), (5, '5p'), (2, '2p'), (1, '1p')]
    for m in payment_methods_verbose(200, coins):
        print m
