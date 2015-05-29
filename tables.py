from strings import *

class Table(object):
    def __init__(self, tableName, headings, values):
        self.tableName  = tableName
        self.headings   = headings
        self.values     = values

    def getOrderedKeys(self):
        unsortedList = []
        sortedList = []
        for key in self.values:
            unsortedList.append(key)
        while unsortedList:
            sortedList.append(min(unsortedList))
            unsortedList.remove(min(unsortedList))
        return sortedList

    def printTable(self):
        rowFormat = "{:<20}" * (len(self.headings) + 1)
        print rowFormat.format("", *self.headings)
        for item in self.getOrderedKeys():
            newList = [item]
            newList.extend(self.values[item])
            rowFormat = "{:<20}" * (len(newList) + 1)
            print rowFormat.format("", *newList)


class STRENGTHTABLE(Table):
    def getStr(self, strengthValue):
        finalStrengthValue = 1
        orderedKeys = self.getOrderedKeys()
        if strengthValue in orderedKeys:
            finalStrengthValue = strengthValue
        elif strengthValue > orderedKeys[-1]:
            finalStrengthValue = 25
        else:
            for i in range(len(orderedKeys)):
                if orderedKeys[i] < strengthValue < orderedKeys[i + 1]:
                    finalStrengthValue = orderedKeys[i]
                    break
        return finalStrengthValue

    def getHitProb(self, strengthValue):
        return self.values[self.getStr(strengthValue)][0]

    def getDamageAdjust(self, strengthValue):
        return self.values[self.getStr(strengthValue)][1]

    def getWeightAllowed(self, strengthValue):
        return self.values[self.getStr(strengthValue)][2]

    def getMaxPress(self, strengthValue):
        return self.values[self.getStr(strengthValue)][3]

    def getOpenDoors(self, strengthValue):
        tries = 1
        values = self.values[self.getStr(strengthValue)]
        openDoors = values[-2]

        if isinstance(openDoors, list):
            tries = openDoors[-1]
            openDoors = openDoors[0]

        return openDoors, tries

    def bendBarLiftGate(self, strengthValue):
        return self.values[self.getStr(strengthValue)][-1]


class DEXTABLE(Table):
    def getDex(self, value):
        return value if 0 < value < 26 else 1 if value < 1 else 25 if value > 25 else None

    def getReactionAdj(self, dexValue):
        return self.values[self.getDex(dexValue)][0]

    def getMissleAttackAdj(self, dexValue):
        return self.values[self.getDex(dexValue)][1]

    def getDefenseAdj(self, dexValue):
        return self.values[self.getDex(dexValue)][2]


class CONTABLE(Table):
    def getCon(self, value):
        return value if 0 < value < 26 else 1 if value < 1 else 25 if value > 25 else None

    def getHitPointAdj(self, convalue):
        realConValue    = self.getCon(convalue)
        warriorAdj      = 0
        minimumDieValue = 1
        values          = self.values[realConValue][0]

        if isinstance(values, list):
            adjust = values[0]
            warriorAdj = values[1]
            minimumDieValue = values[2]
        else:
            adjust = values

        return adjust, warriorAdj, minimumDieValue

    def getSysShock(self, convalue):
        return self.values[self.getCon(convalue)][1]

    def getResSurvival(self, convalue):
        return self.values[self.getCon(convalue)][2]

    def getPoisonSave(self, convalue):
        return self.values[self.getCon(convalue)][3]

    def getRegen(self, convalue):
        return self.values[self.getCon(convalue)][4]

class INTTABLE(Table):
    def getInt(self, value):
        return value if 0 < value < 26 else 1 if value < 1 else 25 if value > 25 else None

    def getNumLangs(self, intvalue):
        return self.values[self.getInt(intvalue)][0]

    def getSpellLevel(self, intvalue):
        return self.values[self.getInt(intvalue)][1]

    def getChanceToLearnSpell(self, intvalue):
        return self.values[self.getInt(intvalue)][2]

    def getMaxSpellsPerLevel(self, intvalue):
        return self.values[self.getInt(intvalue)][3]

    def getIllusionImmunity(self, intvalue):
        realIntValue = self.getInt(intvalue)
        values = []
        for i in range(25):
            curValues = self.values[realIntValue][4]
            if curValues != 0:
                values.append(curValues)
                realIntValue -= 1
            else:
                break
        return values


class WISTABLE(Table):
    def getWisdom(self, value):
        return value if 0 < value < 26 else 1 if value < 1 else 25 if value > 25 else None

    def getMagicDefAdj(self, wisvalue):
        return self.values[self.getWisdom(wisvalue)][0]

    def getBonusSpells(self, wisvalue):
        spellLevels = {1: 0,
                       2: 0,
                       3: 0,
                       4: 0,
                       5: 0,
                       6: 0,
                       7: 0
                       }

        realwisvalue    = self.getWisdom(wisvalue)
        levelList       = []

        for i in range(realwisvalue):
            levelList.extend(self.values[i+1][1])

        for item in levelList:
            if item:
                spellLevels[item] = spellLevels[item] + 1

        return spellLevels

    def getSpellFailureChance(self, wisvalue):
        return self.values[self.getWisdom(wisvalue)][2]

    def getSpellImmunity(self, wisvalue):
        spells = []

        for i in range(self.getWisdom(wisvalue)):
            spells.extend(self.values[i+1][3])

        return spells

class CHATABLE(Table):
    def getCharisma(self, value):
        return value if 0 < value < 26 else 1 if value < 1 else 25

    def getMaxHenchment(self, chavalue):
        return self.values[self.getCharisma(chavalue)][0]

    def getLoyaltyBase(self, chavalue):
        return self.values[self.getCharisma(chavalue)][1]

    def getReactionAdj(self, chavalue):
        return self.values[self.getCharisma(chavalue)][2]

StrTable = STRENGTHTABLE(STR,
                         [TABLE_ABILITYSCORE, TABLE_HIT_PROB, TABLE_DAMAGE_ADJUST, TABLE_WEIGHT_ALLOWED,
                          TABLE_MAX_PRESS, TABLE_OPEN_DOORS, TABLE_BEND_BAR_LIFT_GATE],
                         {1:      [-5, -4,    1,    3,  1,        0],
                          2:      [-3, -2,    1,    5,  1,        0],
                          3:      [-3, -1,    5,   10,  2,        0],
                          4:      [-2, -1,   10,   25,  3,        0],
                          5:      [-2, -1,   10,   25,  3,        0],
                          6:      [-1,  0,   20,   55,  4,        0],
                          7:      [-1,  0,   20,   55,  4,        0],
                          8:      [ 0,  0,   35,   90,  5,        1],
                          9:      [ 0,  0,   35,   90,  5,        1],
                          10:     [ 0,  0,   40,  115,  6,        2],
                          11:     [ 0,  0,   40,  115,  6,        2],
                          12:     [ 0,  0,   45,  140,  7,        4],
                          13:     [ 0,  0,   45,  140,  7,        4],
                          14:     [ 0,  0,   55,  170,  8,        7],
                          15:     [ 0,  0,   55,  170,  8,        7],
                          16:     [ 0,  1,   70,  195,  9,       10],
                          17:     [ 1,  1,   85,  220, 10,       13],
                          18:     [ 1,  2,  110,  255, 11,       16],
                          18.001: [ 1,  3,  135,  280, 12,       20],
                          18.051: [ 2,  3,  160,  305, 13,       25],
                          18.076: [ 2,  4,  185,  330, 14,       30],
                          18.091: [ 2,  5,  235,  380, [15,  3], 35],
                          18.100: [ 3,  6,  335,  480, [16,  6], 40],
                          19:     [ 3,  7,  485,  640, [16,  8], 50],
                          20:     [ 3,  8,  535,  700, [17, 10], 60],
                          21:     [ 4,  9,  635,  810, [17, 12], 70],
                          22:     [ 4, 10,  785,  970, [18, 14], 80],
                          23:     [ 5, 11,  935, 1130, [18, 16], 90],
                          24:     [ 6, 12, 1235, 1440, [19, 17], 95],
                          25:     [ 7, 14, 1535, 1750, [19, 18], 99]
                          }
                         )

DexTable = DEXTABLE(DEX,
                    [TABLE_ABILITYSCORE, TABLE_REACTION_ADJUSTMENT, TABLE_MISSLE_ADJUSTMENT, TABLE_DEFENSE_ADJUSTMENT],
                    {1:  [-6, -6,  5],
                     2:  [-4, -4,  5],
                     3:  [-3, -3,  4],
                     4:  [-2, -2,  3],
                     5:  [-1, -1,  2],
                     6:  [ 0,  0,  1],
                     7:  [ 0,  0,  0],
                     8:  [ 0,  0,  0],
                     9:  [ 0,  0,  0],
                     10: [ 0,  0,  0],
                     11: [ 0,  0,  0],
                     12: [ 0,  0,  0],
                     13: [ 0,  0,  0],
                     14: [ 0,  0,  0],
                     15: [ 0,  0, -1],
                     16: [ 1,  1, -2],
                     17: [ 2,  2, -3],
                     18: [ 2,  2, -4],
                     19: [ 3,  3, -4],
                     20: [ 3,  3, -4],
                     21: [ 4,  4, -5],
                     22: [ 4,  4, -5],
                     23: [ 4,  4, -5],
                     24: [ 5,  5, -6],
                     25: [ 5,  5, -6],
                     }
                    )

ConTable = CONTABLE(CON,
                    [TABLE_ABILITYSCORE, TABLE_HIT_POINT_ADJUSTMENT, TABLE_SYSTEM_SHOCK,
                     TABLE_RESURRECTION_SURVIVAL, TABLE_POISON_SAVE, TABLE_REGEN],
                    {1:  [-3,         25,  30,  -2, 0],
                     2:  [-2,         30,  35,  -1, 0],
                     3:  [-2,         35,  40,  0,  0],
                     4:  [-1,         40,  45,  0,  0],
                     5:  [-1,         45,  50,  0,  0],
                     6:  [-1,         50,  55,  0,  0],
                     7:  [ 0,         55,  60,  0,  0],
                     8:  [ 0,         60,  65,  0,  0],
                     9:  [ 0,         65,  70,  0,  0],
                     10: [ 0,         70,  75,  0,  0],
                     11: [ 0,         75,  80,  0,  0],
                     12: [ 0,         80,  85,  0,  0],
                     13: [ 0,         85,  90,  0,  0],
                     14: [ 0,         88,  92,  0,  0],
                     15: [ 1,         90,  94,  0,  0],
                     16: [ 2,         95,  96,  0,  0],
                     17: [[2, 3, 1],  97,  98,  0,  0],
                     18: [[2, 4, 1],  99, 100,  0,  0],
                     19: [[2, 5, 1],  99, 100,  1,  0],
                     20: [[2, 5, 2],  99, 100,  1,  [1, 6]],
                     21: [[2, 6, 3],  99, 100,  2,  [1, 5]],
                     22: [[2, 6, 3],  99, 100,  2,  [1, 4]],
                     23: [[2, 6, 4],  99, 100,  3,  [1, 3]],
                     24: [[2, 7, 4],  99, 100,  3,  [1, 2]],
                     25: [[2, 7, 4], 100, 100,  4,  [1, 1]]
                     }
                    )

IntTable = INTTABLE(INT,
                    [TABLE_ABILITYSCORE, TABLE_NUM_LANG, TABLE_SPELL_LEVEL,
                     TABLE_CHANCE_TO_LEARN, TABLE_MAX_NUM_OF_SPELLS, TABLE_ILLUSION_IMMUNITY],
                    {1:  [ 0, 0,   0,   0, 0],
                     2:  [ 1, 0,   0,   0, 0],
                     3:  [ 1, 0,   0,   0, 0],
                     4:  [ 1, 0,   0,   0, 0],
                     5:  [ 1, 0,   0,   0, 0],
                     6:  [ 1, 0,   0,   0, 0],
                     7:  [ 1, 0,   0,   0, 0],
                     8:  [ 1, 0,   0,   0, 0],
                     9:  [ 2, 4,  35,   6, 0],
                     10: [ 2, 5,  40,   7, 0],
                     11: [ 2, 5,  45,   7, 0],
                     12: [ 3, 6,  50,   7, 0],
                     13: [ 3, 6,  55,   9, 0],
                     14: [ 4, 7,  60,   9, 0],
                     15: [ 4, 7,  65,  11, 0],
                     16: [ 5, 8,  70,  11, 0],
                     17: [ 6, 8,  75,  14, 0],
                     18: [ 7, 9,  85,  18, 0],
                     19: [ 8, 9,  95, 100, [MAGIC_SCHOOL_ILLUSION, 1]],
                     20: [ 9, 9,  96, 100, [MAGIC_SCHOOL_ILLUSION, 2]],
                     21: [10, 9,  97, 100, [MAGIC_SCHOOL_ILLUSION, 3]],
                     22: [11, 9,  98, 100, [MAGIC_SCHOOL_ILLUSION, 4]],
                     23: [12, 9,  99, 100, [MAGIC_SCHOOL_ILLUSION, 5]],
                     24: [15, 9, 100, 100, [MAGIC_SCHOOL_ILLUSION, 6]],
                     25: [20, 9, 100, 100, [MAGIC_SCHOOL_ILLUSION, 7]],
                     }
                    )

WisTable = WISTABLE(WIS,
                    [TABLE_ABILITYSCORE, TABLE_MAGIC_DEF_ADJUSTMENT, TABLE_BONUS_SPELLS,
                     TABLE_CHANCE_SPELL_FAILURE, TABLE_SPELL_IMMUNITY],
                    {1:  [-6,    [], 80,  []],
                     2:  [-4,    [], 60,  []],
                     3:  [-3,    [], 50,  []],
                     4:  [-2,    [], 45,  []],
                     5:  [-1,    [], 40,  []],
                     6:  [-1,    [], 35,  []],
                     7:  [-1,    [], 30,  []],
                     8:  [ 0,    [], 25,  []],
                     9:  [ 0,    [], 20,  []],
                     10: [ 0,    [], 15,  []],
                     11: [ 0,    [], 10,  []],
                     12: [ 0,    [],  5,  []],
                     13: [ 0,    [1],  0, []],
                     14: [ 0,    [1],  0, []],
                     15: [ 1,    [2],  0, []],
                     16: [ 2,    [2],  0, []],
                     17: [ 3,    [3],  0, []],
                     18: [ 4,    [4],  0, []],
                     19: [ 4, [1, 3],  0, ['cause fear', 'charm person', 'command', 'friends', 'hypnotism']],
                     20: [ 4, [2, 4],  0, ['forget', 'hold person', 'ray of enfeeblement', 'scare']],
                     21: [ 4, [3, 5],  0, ['fear']],
                     22: [ 4, [4, 5],  0, ['charm monster', 'confusion', 'emotion', 'fumble', 'suggestion']],
                     23: [ 4, [1, 6],  0, ['chaos', 'feeblemind', 'hold monster', 'magic jar', 'quest']],
                     24: [ 4, [5, 6],  0, ['geas', 'mass suggestion', 'rod of rulership']],
                     25: [ 4, [6, 7],  0, ['antipathy', 'sympathy', 'death spell', 'mass charm']],
                     }
                    )

ChaTable = CHATABLE(CHA,
                    [TABLE_ABILITYSCORE, TABLE_MAX_HENCMEN,
                     TABLE_LOYALTY_BASE, TABLE_SOCIAL_REACTION_ADJUSTMENT],
                    {1:  [ 0, -8, -7],
                     2:  [ 1, -7, -6],
                     3:  [ 1, -6, -5],
                     4:  [ 1, -5, -4],
                     5:  [ 2, -4, -3],
                     6:  [ 2, -3, -2],
                     7:  [ 3, -2, -1],
                     8:  [ 3, -1,  0],
                     9:  [ 4,  0,  0],
                     10: [ 4,  0,  0],
                     11: [ 4,  0,  0],
                     12: [ 5,  0,  0],
                     13: [ 5,  0,  1],
                     14: [ 6,  1,  2],
                     15: [ 7,  3,  3],
                     16: [ 8,  4,  5],
                     17: [10,  6,  6],
                     18: [15,  8,  7],
                     19: [20, 10,  8],
                     20: [25, 12,  9],
                     21: [30, 14, 10],
                     22: [35, 16, 11],
                     23: [40, 18, 12],
                     24: [45, 20, 13],
                     25: [50, 20, 14],
                     }
                    )