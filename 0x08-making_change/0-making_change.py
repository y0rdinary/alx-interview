#!/usr/bin/python3


def makeChange(coins, total):
        count_amount = 0
        count_coins = 0
        if total <= 0:
            return 0
        else:
            while count_amount < total:
                if len(coins) == 0:
                    return -1
                count_amount += max(coins)
                if count_amount > total:
                    count_amount -= max(coins)
                    coins.remove(max(coins))
                else:
                    count_coins += 1

        return count_coins
