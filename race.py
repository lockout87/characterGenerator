import dice
import CLASS

class race():
    def __init__(self, raceName, classRestrictions, statRestrictions, statAdjustments,
                 heightRange, weightRange, ageRange):
        assert isinstance(raceName, str),           "raceName must be of type str"
        assert isinstance(classRestrictions, list), "classRestrictions must be of type list"
        assert isinstance(statRestrictions, dict),  "statRestrictions must be of type dict"
        assert isinstance(statAdjustments, dict),   "statAdjustments must be of type dict"
        assert isinstance(heightRange, str),        "heightRange must be of type str"
        assert isinstance(weightRange, str),        "weightRange must be of type str"
        assert isinstance(ageRange, str),           "ageRange must be of type str"
        
        self.raceName           = raceName
        self.classRestrictions  = classRestrictions
        self.statRestriction    = statRestrictions
        self.statAdjustments    = statAdjustments
        self.heightRange        = heightRange
        self.weightRange        = weightRange
        self.ageRange           = ageRange

    def generateClass(self):
        pass

    def generateStats(self):
        pass

    def generateCharacter(self):
        character = {"raceName":    self.raceName,
                     "class":       self.generateClass(),
                     "stats":       self.generateStats(),
                     "height":      dice.zPlusxdy(self.heightRange),
                     "weight":      dice.zPlusxdy(self.weightRange),
                     "age":         dice.zPlusxdy(self.ageRange),
                     }
        return character