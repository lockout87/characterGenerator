__author__ = 'lockout87'

import random


def shuffler(dieSize):
    shuffleRange = range(dieSize)
    random.shuffle(shuffleRange)
    return shuffleRange[0] + 1

def xDx(xDx):
    xDx = xDx.upper()
    numberOfDice    = int(xDx.split("D")[0])
    dieSize         = int(xDx.split("D")[1])

    total = 0

    for i in range(numberOfDice):
        total += shuffler(dieSize)
    return total

def fourDSixDropLowest():
    rolls = [xDx("1D6") for i in range(4)]
    rolls.remove(min(rolls))
    return sum(rolls)
