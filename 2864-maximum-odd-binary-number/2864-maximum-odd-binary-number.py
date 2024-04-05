class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        onescount = 0
        zeroescount = 0
        
        for num in s:
            temp = (int)(num)
            if temp == 1:
                onescount = onescount + 1
            else:
                zeroescount = zeroescount + 1
        
        result = []
        while onescount > 1:
            result.append("1")
            onescount = onescount - 1
        
        while zeroescount > 0:
            result.append("0")
            zeroescount = zeroescount - 1
        
        result.append("1")
        return "".join(result)