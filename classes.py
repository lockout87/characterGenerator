__author__ = 'lockout87'


class classes():
    def __init__(self, className, hitDie, statRestrictions, thac0Progression, bonusConHP = False, bonusStr = False):
        assert isinstance(className, str),          "className must be of type str"
        assert isinstance(hitDie, int),             "hitDie must be of type int"
        assert isinstance(statRestrictions, dict),  "statRestrictions must be of type dict"
        assert isinstance(bonusConHP, bool),        "bonusConHP must be of type bool"
        assert isinstance(bonusStr, bool),          "bonusStr must be of type bool"

        self.className          = className
        self.statRestrictions   = statRestrictions
        self.hitDie             = hitDie
        self.bonusConHP         = bonusConHP
        self.thac0Progression   = thac0Progression
        self.bonusStr           = bonusStr


    def rollHP(self, level):
        hp = hitDie + "{}"




