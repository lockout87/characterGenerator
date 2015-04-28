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
        rowFormat = "{:>15}" * (len(self.headings))
        print rowFormat.join(self.headings)
        row = ""
        for item in self.getOrderedKeys():





StrengthTable = Table("Strength",
                      ["Ability Score", "Hit Prob", "Damage Adjustment", "Weight Allowed",
                       "Max Press", "Open Doors", "Bend Bars/LiftGates"],
                      {1:      [-5, -4,   1,   3,  1,   0],
                       2:      [-3, -2,   1,   5,  1,   0],
                       3:      [-3, -1,   5,  10,  2,   0],
                       4:      [-2, -1,  10,  25,  3,   0],
                       #5:      [-2, -1,  10,  25,  3,   0],
                       6:      [-1,  0,  20,  55,  4,   0],
                       #7:      [-1,  0,  20,  55,  4,   0],
                       8:      [ 0,  0,  35,  90,  5,   1],
                       #9:      [ 0,  0,  35,  90,  5,   1],
                       10:     [ 0,  0,  40, 115,  6,   2],
                       #11:     [ 0,  0,  40, 115,  6,   2],
                       12:     [ 0,  0,  45, 140,  7,   4],
                       #13:     [ 0,  0,  45, 140,  7,   4],
                       14:     [ 0,  0,  55, 170,  8,   7],
                       #15:     [ 0,  0,  55, 170,  8,   7],
                       16:     [ 0,  1,  70, 195,  9,  10],
                       17:     [ 1,  1,  85, 220, 10,  13],
                       18:     [ 1,  2, 110, 255, 11,  16],
                       18.001: [ 1,  3, 135, 280, 12,  20],
                       18.051: [ 2,  3, 160, 305, 13,  25],
                       18.076: [ 2,  4, 185, 330, 14,  30],
                       18.091: [ 2,  5, 235, 380, 15,  35],
                       18.100: [ 3,  6, 335, 480, [15, 3],  35],
                       19:     [ 3,  7, 485, 640, [16, 6],  40],
                       }
                      )


StrengthTable.getOrderedKeys()
#StrengthTable.printTable()