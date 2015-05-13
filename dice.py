__author__ = 'lockout87'

from random import shuffle
from collections import Counter

def shuffler(dieSize):
    """
    Shuffles the numbers and selects the "top".
    Uses random shuffle due to small die size.
    :param dieSize:
    :return int:
    """
    shuffleRange = range(dieSize)
    shuffle(shuffleRange)
    return shuffleRange[0] + 1


def xdy(xDy):
    """
    Rolls x number of y-sized dice. Returns the sum.
    :param xDy:
    :return:
    """
    assert isinstance(xDy, str), "xDx should be of type string"
    xDeey = xDy.upper()

    numberOfDice    = int(xDeey.split("D")[0])
    dieSize         = int(xDeey.split("D")[1])

    return sum([shuffler(dieSize) for _ in range(numberOfDice)])


def xdyrz(xDyRz):
    """
    Rolls x number of y-sized dice. Rerolls if result is less than z.
    :param xDyRz:
    :return:
    """
    xDy, z = xDyRz.split("R")
    x, y = xDy.split("D")
    sum = 0
    for _ in range(int(x)):
        sum += shuffler(int(y)-int(z)) + int(z)

    return sum


def zPlusxdy(zxDy):
    z, xDy = zxDy.split("+")
    return int(z) + xdy(xDy)

def fourDSixDropLowest():
    """
    Generally used for stat generation. fourDSixDropLowest returns the sum of 3 six-sided dice,
    after rolling four and dropping the lowest.
    :return:
    """
    rolls = [xdy("1D6") for _ in range(4)]
    rolls.remove(min(rolls))
    return sum(rolls)


def diceUnitTests():
    assert Counter([fourDSixDropLowest() for _ in range(50000)]).most_common()[0][0] == 13, \
        "Most common number from fourDSixDropLowest() should always be 13. A portion of the stack has been broken."
