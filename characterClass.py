import classes as CLASS
from strings import *

__author__ = 'lockout87'

class characterClass():
    def __init__(self):
        self.fighter        = CLASS.classes(FIGHTER,
                                            10,
                                            {STR: 9},
                                            [1, 1],
                                            bonusConHP = True,
                                            bonusStr = True
                                            )
        self.paladin        = CLASS.classes(PALADIN,
                                            10,
                                            {STR: 12, CON: 9, WIS: 13, CHA:17},
                                            [1, 1],
                                            bonusConHP = True,
                                            bonusStr = True
                                            )
        self.ranger         = CLASS.classes(RANGER,
                                            10,
                                            {STR: 13, DEX: 13, CON: 14, WIS: 14},
                                            [1, 1],
                                            bonusConHP = True,
                                            bonusStr = True
                                            )
        # Wizards
        self.mage           = CLASS.classes(MAGE,
                                            4,
                                            {INT: 9},
                                            [1, 4]
                                            )
        self.abjurer        = CLASS.classes(ABJURER,
                                            4,
                                            {INT: 9, WIS: 15},
                                            [1, 4]
                                            )
        self.conjurer       = CLASS.classes(CONJURER,
                                            4,
                                            {INT: 9, CON: 15},
                                            [1, 4]
                                            )
        self.diviner        = CLASS.classes(DIVINER,
                                            4,
                                            {INT: 9, WIS: 16},
                                            [1, 4]
                                            )
        self.enchanter      = CLASS.classes(ENCHANTER,
                                            4,
                                            {INT: 9, CHA: 16},
                                            [1, 4]
                                            )
        self.illusionist    = CLASS.classes(ILLUSIONIST,
                                            4,
                                            {INT: 9, DEX: 16},
                                            [1, 4]
                                            )
        self.invoker        = CLASS.classes(INVOKER,
                                            4,
                                            {INT: 9, CON: 16},
                                            [1, 4]
                                            )
        self.necromancer    = CLASS.classes(NECROMANCER,
                                            4,
                                            {INT: 9, WIS: 16},
                                            [1, 4]
                                            )
        self.transmuter     = CLASS.classes(TRANSMUTER,
                                            4,
                                            {INT: 9, DEX: 15},
                                            [1, 4]
                                            )
        # Clerics
        self.priest         = CLASS.classes(PRIEST,
                                            8,
                                            {WIS: 9},
                                            [2, 3]
                                            )
        self.druid          = CLASS.classes(DRUID,
                                            8,
                                            {WIS: 9},
                                            [2, 3]
                                            )
        # Rogues
        self.bard           = CLASS.classes(BARD,
                                            6,
                                            {DEX: 12, INT: 13, CHA: 15},
                                            [1, 2]
                                            )
        self.thief          = CLASS.classes(THIEF,
                                            6,
                                            {DEX: 9},
                                            [1, 2]
                                            )

CLASSES = characterClass()
