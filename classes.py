import dice
import tables
from strings import *

class classes():
    def __init__(self, className, hitDie, statRestrictions, thac0Progression, bonusConHP = False, bonusStr = False):
        assert isinstance(className, str),          CLASS_CLASSNAME_WAR
        assert isinstance(hitDie, int),             CLASS_HITDIE_WAR
        assert isinstance(statRestrictions, dict),  CLASS_STATRESTRICT_WAR
        assert isinstance(bonusConHP, bool),        CLASS_BONUSCON_WAR
        assert isinstance(bonusStr, bool),          CLASS_BONUSSTR_WAR

        self.className          = className
        self.statRestrictions   = statRestrictions
        self.hitDie             = hitDie
        self.bonusConHP         = bonusConHP
        self.thac0Progression   = thac0Progression
        self.bonusStr           = bonusStr

    def rollHP(self, level, stats):
        hpAdjust, warriorAdjust, minimumValue = tables.ConTable.getHitPointAdj(stats[CON])
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


