class Solution:
    def myAtoi(self, s: str) -> int:
        digits = {
            '0': True,
            '1': True,
            '2': True,
            '3': True,
            '4': True,
            '5': True,
            '6': True,
            '7': True,
            '8': True,
            '9': True
        }
        
        digitsRead = []
        
        slist = list(s)
        negative = False
        start = None
        
        for character in slist:
            if character == ' ' and start == None:
                continue
                
            elif character == '-' or character == '+':
                if start == None:
                    if character == '-':
                        negative = True
                    start = True
                else:
                    break
        
            elif (character) in digits:
                digitsRead.append(int(character))
                start = True
            else:
                break
        
        
        power  = len(digitsRead) - 1
        sum = 0
        for digit in digitsRead:
            sum = sum + (digit * (10 ** power))
            power = power - 1
        
        if negative:
            sum = sum * -1
        
        lowestMin = ((2 ** 31) * -1)
        if sum < lowestMin:
            return lowestMin
        
        higestMax = ((2 ** 31) - 1)
        if sum > higestMax:
            return higestMax
        
        return sum
            