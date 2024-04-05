class Solution:
    def makeGood(self, s: str) -> str:
        hashmap = {}
        for position, character in enumerate(s):
            # ADD THE CHARACTER INTO THE HASHMAP
            hashmap[position] = character
            
            # RETRIEVE THE PREVIOUS POSITION
            previous_position = position - 1
            
            # IF THE PREVIOUS POSITION IN HASHMAP THEN CHECK FOR THE PROBLEM CONDITION
            if previous_position in hashmap:
                previousvalue = hashmap[previous_position]
                currentvalue = character
                finalcondition = self.checkCondition(previousvalue , currentvalue)
                
                if finalcondition:
                    del hashmap[previous_position]
                    del hashmap[position]
                                
        print(hashmap)
        
        result = []
        count = 0
        for key in hashmap:
            if count == 0:
                result.append(hashmap[key])
                count = count + 1
            else:
                poppedvalue = result.pop()
                count = count - 1
                
                finalcondition = self.checkCondition(poppedvalue , hashmap[key])
                if finalcondition:
                    continue
                else:
                    result.append(poppedvalue)
                    result.append(hashmap[key])
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
        