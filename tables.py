__author__ = 'lockout87'

class Table():
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
    def getDex(self, dexvalue):
        return dexvalue

    def getReactionAdj(self, dexValue):
        return self.values[self.getDex(dexValue)][0]

    def getMissleAttackAdj(self, dexValue):
        return self.values[self.getDex(dexValue)][1]

    def getDefenseAdj(self, dexValue):
        return self.values[self.getDex(dexValue)][2]


class CONTABLE(Table):
    def getCon(self, convalue):
        if convalue < 1:
            convalue = 1
        elif convalue > 25:
            convalue = 25
        return convalue

    def getHitPointAdj(self, convalue):
        realConValue    = self.getCon(convalue)
        warriorAdj      = 0
        minimumDieValue = 1
        values          = self.values[realConValue]

        if isinstance(values, list):
            adjust = values[0]
            warriorAdj = values[1]
            minimumDieValue = values[2]
        else:
            adjust = values

        return adjust, warriorAdj, minimumDieValue




StrTable = STRENGTHTABLE("Strength",
                         ["Ability Score", "Hit Prob", "Damage Adjustment", "Weight Allowed",
                          "Max Press", "Open Doors", "Bend Bars/LiftGates"],
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

DexTable = DEXTABLE("Dexterity",
                    ["Ablity Score", "Reaction Adj.", "Missle Attack Adj.", "Defensive Adj."],
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

ConTable = CONTABLE("Constitution",
                    ["Ability Score", "Hit Point Adj.", "System Shock", "Resurrection Survival", "Poison Save", "Regeneration"],
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
                     17: [[2, 3],     97,  98,  0,  0],
                     18: [[2, 4],     99, 100,  0,  0],
                     19: [[2, 5],     99, 100,  1,  0],
                     20: [[2, 5, 2],  99, 100,  1,  [1, 6]],
                     21: [[2, 6, 3],  99, 100,  2,  [1, 5]],
                     22: [[2, 6, 3],  99, 100,  2,  [1, 4]],
                     23: [[2, 6, 4],  99, 100,  3,  [1, 3]],
                     24: [[2, 7, 4],  99, 100,  3,  [1, 2]],
                     25: [[2, 7, 4], 100, 100,  4,  [1, 1]]
                     }
                    )