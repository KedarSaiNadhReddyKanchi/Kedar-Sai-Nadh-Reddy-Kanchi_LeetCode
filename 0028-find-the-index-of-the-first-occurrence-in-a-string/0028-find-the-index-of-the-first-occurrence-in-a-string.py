class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        first_characterin_needle = needle[0]
        needle_length = len(needle)
        
        haystackmap = {}
        for index , haystackcharacter in enumerate(haystack):
            if haystackcharacter ==  first_characterin_needle:
                haystackmap[index] = "" + haystackcharacter
        
        for index in haystackmap:
            substring1 = haystack[index : (index + needle_length)]
            if substring1 == needle:
                return index
        return -1
        
