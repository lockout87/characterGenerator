import classes as CLASS

__author__ = 'lockout87'

class characterClass():
    def __init__(self):
        self.fighter        = CLASS.classes("fighter",
                                            10,
                                            {"str": 9},
                                            [1, 1],
                                            bonusConHP = True,
                                            bonusStr = True
                                            )
        self.paladin        = CLASS.classes("paladin",
                                            10,
                                            {"str": 12, "con": 9, "wis": 13, "cha":17},
                                            [1, 1],
                                            bonusConHP = True,
                                            bonusStr = True
                                            )
        self.ranger         = CLASS.classes("ranger",
                                            10,
                                            {"str": 13, "dex": 13, "con": 14, "wis": 14},
                                            [1, 1],
                                            bonusConHP = True,
                                            bonusStr = True
                                            )
        # Wizards
        self.mage           = CLASS.classes("mage",
                                            4,
                                            {"int": 9},
                                            [1, 4]
                                            )
        self.abjurer        = CLASS.classes("abjurer",
                                            4,
                                            {"int": 9, "wis": 15},
                                            [1, 4]
                                            )
        self.conjurer       = CLASS.classes("conjurer",
                                            4,
                                            {"int": 9, "con": 15},
                                            [1, 4]
                                            )
        self.diviner        = CLASS.classes("diviner",
                                            4,
                                            {"int": 9, "wis": 16},
                                            [1, 4]
                                            )
        self.enchanter      = CLASS.classes("enchanter",
                                            4,
                                            {"int": 9, "cha": 16},
                                            [1, 4]
                                            )
        self.illusionist    = CLASS.classes("illusionist",
                                            4,
                                            {"int": 9, "dex": 16},
                                            [1, 4]
                                            )
        self.invoker        = CLASS.classes("invoker",
                                            4,
                                            {"int": 9, "con": 16},
                                            [1, 4]
                                            )
        self.necromancer    = CLASS.classes("necromancer",
                                            4,
                                            {"int": 9, "wis": 16},
                                            [1, 4]
                                            )
        self.transmuter     = CLASS.classes("transmuter",
                                            4,
                                            {"int": 9, "dex": 15},
                                            [1, 4]
                                            )
        # Clerics
        self.priest         = CLASS.classes("priest",
                                            8,
                                            {"wis": 9},
                                            [2, 3]
                                            )
        self.druid          = CLASS.classes("druid",
                                            8,
                                            {"wis": 9},
                                            [2, 3]
                                            )
        # Rogues
        self.bard           = CLASS.classes("bard",
                                            6,
                                            {"dex": 12, "int": 13, "cha": 15},
                                            [1, 2]
                                            )
        self.thief          = CLASS.classes("thief",
                                            6,
                                            {"dex": 9},
                                            [1, 2]
                                            )

CLASSES = characterClass()