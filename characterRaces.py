import race


assert isinstance(raceName, str),           "raceName must be of type str"
assert isinstance(classRestrictions, list), "classRestrictions must be of type list"
assert isinstance(statRestrictions, dict),  "statRestrictions must be of type dict"
assert isinstance(statAdjustments, dict),   "statAdjustments must be of type dict"
assert isinstance(heightRange, str),        "heightRange must be of type str"
assert isinstance(weightRange, str),        "weightRange must be of type str"
assert isinstance(ageRange, str),           "ageRange must be of type str"


class characterRaces():
    def __init__(self):
        self.elf    = race.race("elf",
                                ["fighter", "priest", "thief", "mage"],
                                {"str": [3, 18],
                                 "dex": [6,18],
                                 "con": [7, 18],
                                 "int": [8, 18],
                                 "wis": [3, 18],
                                 "cha": [8, 18]
                                 },
                                {"dex": 1, "con": -1},


                                )