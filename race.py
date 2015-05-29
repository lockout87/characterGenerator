import dice
import classes
from strings import *

class race():
    def __init__(self, raceName, classRestrictions, statRestrictions, statAdjustments,
                 heightRange, weightRange, ageRange):
        assert isinstance(raceName, str),           RACE_RACE_NAME_WAR
        assert isinstance(classRestrictions, list), RACE_CLASS_RESTRICTION_WAR
        assert isinstance(statRestrictions, dict),  RACE_STAT_RESTRICTION_WAR
        assert isinstance(statAdjustments, dict),   RACE_STAT_ADJUSTMENT_WAR
        assert isinstance(heightRange, str),        RACE_HEIGHT_RANGE_WAR
        assert isinstance(weightRange, str),        RACE_WEIGHT_RANGE_WAR
        assert isinstance(ageRange, str),           RACE_AGE_RANGE_WAR
        
        self.raceName           = raceName
        self.classRestrictions  = classRestrictions
        self.statRestriction    = statRestrictions
        self.statAdjustments    = statAdjustments
        self.heightRange        = heightRange
        self.weightRange        = weightRange
        self.ageRange           = ageRange

    def generateCharacterRace(self, stats):
        character = None
        if self.statsFit(stats):
            character = {"raceName":    self.raceName,
                         "height":      dice.zPlusxdy(self.heightRange),
                         "weight":      dice.zPlusxdy(self.weightRange),
                         "age":         dice.zPlusxdy(self.ageRange),
                         }

        return character

    def statsFit(self, stats):
        statsAreGood = True
        for statName, statValue in self.statRestriction.iteritems():
            if stateValue >= stats[statName]:
                continue
            else:
                statsAreGood = False
                break

        return statsAreGood



