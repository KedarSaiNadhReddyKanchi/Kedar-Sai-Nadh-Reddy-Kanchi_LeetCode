class Solution:
    def makeGood(self, s: str) -> str:
        result = []
        count = 0
        for character in s:
            if count == 0:
                result.append(character)
                count = count + 1
            else:
                poppedvalue = result.pop()
                count = count - 1
                
                finalcondition = self.checkCondition(poppedvalue , character)
                if finalcondition:
                    continue
                else:
                    result.append(poppedvalue)
                    result.append(character)
                    count = count + 2
        
        print(result)
        return "".join(result)
        
        

        
    def checkCondition(self, prev, curr):
        prevcondition = prev.isupper()
        currcondition = curr.isupper()
        
        if ((prevcondition == True) and (currcondition == True)):
            return False
        
        if ((prevcondition == False) and (currcondition == False)):
            return False
        
        condition1 = prevcondition or currcondition
        condition2 = prev.lower() == curr.lower()
        
        if condition1 and condition2:
            return True
        
        return False