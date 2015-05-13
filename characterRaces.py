import race
import characterClass


class characterRaces():
    def __init__(self):
        self.elf    = race.race("elf",
                                [characterClass.CLASSES.fighter,
                                 characterClass.CLASSES.priest,
                                 characterClass.CLASSES.thief,
                                 characterClass.CLASSES.mage
                                 ],
                                {"str": [3, 18],
                                 "dex": [6,18],
                                 "con": [7, 18],
                                 "int": [8, 18],
                                 "wis": [3, 18],
                                 "cha": [8, 18]
                                 },
                                {"dex": 1, "con": -1},
                                )