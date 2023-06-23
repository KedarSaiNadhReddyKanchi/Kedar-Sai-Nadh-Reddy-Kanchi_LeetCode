class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        strlist = list(s)
        position = len(strlist) - 1
        
        newstrlist = []
        
        for start in range(0 , len(strlist)):
            character = strlist[start]
            if character.isalnum():
                if character.isalpha():
                    newstrlist.append(lower(character))
                else:
                    newstrlist.append((character))
                    
        start = 0
        end = len(newstrlist) - 1
        flag = True
        while start <= end:
            if newstrlist[start] != newstrlist[end]:
                flag = False
                break
            start = start + 1
            end = end - 1
                
        
        return flag
                
                    
                
                
            