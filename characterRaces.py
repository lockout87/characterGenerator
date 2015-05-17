import race
import characterClass
from stats import *


(self, raceName, classRestrictions, statRestrictions, statAdjustments,
                 heightRange, weightRange, ageRange)

class characterRaces():
    def __init__(self):
        self.elf    = race.race("elf",
                                [characterClass.CLASSES.fighter,
                                 characterClass.CLASSES.priest,
                                 characterClass.CLASSES.thief,
                                 characterClass.CLASSES.mage
                                 ],
                                {str: [3, 18],
                                 dex: [6,18],
                                 con: [7, 18],
                                 int: [8, 18],
                                 wis: [3, 18],
                                 cha: [8, 18]
                                 },
                                {dex: 1, con: -1},
                                "55+1D10",
                                "90+3D10",
                                "100+5D6"
                                )

        self.dwarf  = race.race("dwarf",
                                [characterClass.CLASSES.fighter,
                                 characterClass.CLASSES.priest,
                                 characterClass.CLASSES.thief,
                                 ],
                                {str: [8, 18],
                                 dex: [3, 17],
                                 con: [11, 18],
                                 int: [3, 18],
                                 wis: [3, 18],
                                 cha: [3, 17],
                                 }, {}
                                )