class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        # totallength = len(s)
        # if totallength % 2 != 0 or totallength % 3 != 0 or totallength % 5 != 0:
        #     return False
        
        partition = []
        strlist = list(s)
        # print(strlist)
        totallength = len(s)     
        
        for letter in strlist:
            partition.append(letter)
            temp = []
            
            stringtoappend = "".join(partition)
            partitionlength = len(stringtoappend)
            numberoftimestoappend = None
            
            if (totallength % partitionlength == 0):
                numberoftimestoappend = int(totallength / partitionlength)
                if numberoftimestoappend > 1:
                    for index in range(numberoftimestoappend):
                        temp.append(stringtoappend)

                    formedstring = "".join(temp)
                    if formedstring == s:
                        return True
            
        return False   
            
            
        
        