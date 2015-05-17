import race 
import characterClass
import characterRaces
import dice
import classes
import tables
from stats import *

class character(object):
    def __init__(self):
        self._stats = self.generateStats()
        self._race  = self.generateRace(self._stats)
        #self._class = self.generateClass(self._stats, self._race)

    def generateStats(self):
        statsNames  = [str, dex, con, int, wis, cha]
        statNumbers = [dice.fourDSixDropLowest() for _ in range(6)]
        statDict    = {name: number for name, number in zip(statsNames, statNumbers)}
        return statDict

    def getStats(self):
        return self._stats

    def generateRace(self, stats):
        while True:



