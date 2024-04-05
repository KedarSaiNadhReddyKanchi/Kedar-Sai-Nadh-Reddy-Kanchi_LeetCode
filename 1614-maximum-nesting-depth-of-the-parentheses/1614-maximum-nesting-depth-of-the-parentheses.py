class Solution:
    def maxDepth(self, s: str) -> int:
        start = 0
        highest_nesting = 0
        
        for character in s:
            if character == "(":
                # do something
                start = start + 1
                if start > highest_nesting:
                    highest_nesting = start
            elif character == ")":
                # do something
                start = start - 1
            else:
                continue
        
        return highest_nesting
        
        