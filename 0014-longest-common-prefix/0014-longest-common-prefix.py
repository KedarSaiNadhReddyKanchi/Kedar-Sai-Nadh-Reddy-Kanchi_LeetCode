class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sortedList = sorted(strs, key=lambda x: len(x))
        print(sortedList)
        
        shortString = sortedList[0]
        new_position = 0
        
        for position , word in enumerate(sortedList):
            if position > 0:
                strList = list(word)
                shortString_length = len(shortString)
                index = 0
                while index < shortString_length:
                    if shortString[index] == strList[index]:
                        index = index + 1
                    else:
                        if index == 0:
                            return ""
                        else:
                            shortString = shortString[0 : index]
                            index = shortString_length
                
        return (shortString)
                
                    
                            
                            
                    
            
        