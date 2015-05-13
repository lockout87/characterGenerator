import dice
import tables


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

    def rollHP(self, level, stats):
        hpAdjust, warriorAdjust, minimumValue = tables.ConTable.getHitPointAdj(stats["con"])
        hpAdjust = hpAdjust if not self.bonusConHP else warriorAdjust
        return dice.xdyrz("{}D{}R{}".format(level-1, self.hitDie, minimumValue)) + level * hpAdjust + self.hitDie

    def checkStats(self, stats):
        statsFit = True
        for key in self.statRestrictions:
            if key in stats:
                if stats[key] < self.statRestrictions[key]:
                    statsFit = False
        return statsFit

    def getThac0(self, level):
        return 20 - self.thac0Progression[0] * ((level - 1) / self.thac0Progression[1])


