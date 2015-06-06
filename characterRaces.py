import race
import characterClass
from strings import *


class characterRaces():
    def __init__(self):
        self.elf    = race.race(ELF,
                                [characterClass.CLASSES.fighter,
                                 characterClass.CLASSES.priest,
                                 characterClass.CLASSES.thief,
                                 characterClass.CLASSES.mage
                                 ],
                                {STR: [3, 18],
                                 DEX: [6,18],
                                 CON: [7, 18],
                                 INT: [8, 18],
                                 WIS: [3, 18],
                                 CHA: [8, 18]
                                 },
                                {DEX: 1, CON: -1},
                                "55+1D10",
                                "90+3D10",
                                "100+5D6"
                                )

        self.dwarf  = race.race(DWARF,
                                [characterClass.CLASSES.fighter,
                                 characterClass.CLASSES.priest,
                                 characterClass.CLASSES.thief,
                                 ],
                                {STR: [8, 18],
                                 DEX: [3, 17],
                                 CON: [11, 18],
                                 INT: [3, 18],
                                 WIS: [3, 18],
                                 CHA: [3, 17],
                                 },
                                {CON: 1, CHA: -1},
                                "45+1D10",
                                "115+1D110",
                                "55+5D6"
                                )
        self.characterRaces = [self.dwarf, self.elf]

CHARACTER_RACES = characterRaces()
