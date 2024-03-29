class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        hashmap = {
            1: 'A',
            2: 'B',
            3: 'C',
            4: 'D',
            5: 'E',
            6: 'F',
            7: 'G',
            8: 'H',
            9: 'I',
            10: 'J',
            11: 'K',
            12: 'L',
            13: 'M',
            14: 'N',
            15: 'O',
            16: 'P',
            17: 'Q',
            18: 'R',
            19: 'S',
            20: 'T',
            21: 'U',
            22: 'V',
            23: 'W',
            24: 'X',
            25: 'Y',
            26: 'Z',
            0: 'Z'
        }
        
        if columnNumber <= 26:
            return hashmap[columnNumber]
        else:
            columnName = []
            remainder = 0
            while columnNumber > 26:
                remainder = int(columnNumber % 26)
                columnName.append(hashmap[remainder])
                columnNumber = int(columnNumber / 26)
                if remainder == 0:
                    columnNumber = columnNumber - 1
            if columnNumber != 0:
                columnName.append(hashmap[columnNumber])
                columnNumber = 0
            columnName = columnName[::-1]
            return "".join(columnName)
                
        