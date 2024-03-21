class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        versionlist1 = version1.split(".")
        versionlist2 = version2.split(".")
        
        versionlength1 = len(versionlist1)
        versionlength2 = len(versionlist2)
        
        position = 0
        difference = None
        
        while ((position < versionlength1) and (position < versionlength2)):
            value1 = (int)(versionlist1[position])
            value2 = (int)(versionlist2[position])
            
            if value1 > value2:
                return 1
            elif value1 < value2:
                return -1
            else:
                difference = 0
            
            position = position + 1
        
        if position == versionlength1:
            defaultvalue = 0
            while position < versionlength2:
                value2 = (int)(versionlist2[position])
                if value2 > defaultvalue:
                    return -1
                elif value2 < defaultvalue:
                    return 1
                else:
                    difference = 0
                position = position + 1
        
        elif position == versionlength2:
            defaultvalue = 0
            while position < versionlength1:
                value1 = (int)(versionlist1[position])
                if value1 > defaultvalue:
                    return 1
                elif value1 < defaultvalue:
                    return -1
                else:
                    difference = 0
                position = position + 1
        
        return 0; 
                
        