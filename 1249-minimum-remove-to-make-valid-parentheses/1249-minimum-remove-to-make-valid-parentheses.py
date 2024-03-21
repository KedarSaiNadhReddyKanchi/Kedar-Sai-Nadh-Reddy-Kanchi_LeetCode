class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        left = 0
        right = 0 
        array = []
        problematic_indices = []
        slist = list(s)
        
        for position, character in enumerate(s):
            if character == "(":
                left = left + 1
                array.append(["(", position])
            elif character == ")":
                # right = right + 1
                # array.append([")", position])
                if left == 0:
                    problematic_indices.append(position)
                else:
                    if left > 0:
                        array.pop()
                        left = left - 1
                    
            else:
                continue
        
        # print(f"left = {left} and right = {right}")
        
        if left != 0:
            for pair in array:
                position = pair[1]
                slist[position] = ""
        
        for index in problematic_indices:
            slist[index] = ""
        
        result = "".join(slist)
        return result
        