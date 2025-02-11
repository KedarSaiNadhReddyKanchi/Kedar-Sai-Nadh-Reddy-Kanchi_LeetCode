class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        size = len(s)
        part_string_size = len(part)

        while size >= part_string_size:
            # find the index of the part string in the string s
            index = s.find(part)
            if index == -1:
                return s
            else:
                start , end = index , index + part_string_size
                new_string = s[0 : start] + s[end : ]
                size = size - part_string_size
                s = new_string
        
        return s