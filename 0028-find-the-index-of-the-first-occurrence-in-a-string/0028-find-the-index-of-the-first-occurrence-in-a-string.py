class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        # need to implement sliding window concept
        needle_pointer = 0
        last_haystack_pointer = -1
        needle_length = len(needle)
        haystack_length = len(haystack)
        substring_length_found = 0
        haystack_pointer = 0
        
        while haystack_pointer < haystack_length :
            
            if haystack[haystack_pointer] == needle[needle_pointer]:
                if needle_pointer == 0:
                    last_haystack_pointer = haystack_pointer
                    
                needle_pointer = needle_pointer + 1
                substring_length_found = substring_length_found + 1
                if substring_length_found == needle_length:
                    return last_haystack_pointer
                else:
                    haystack_pointer = haystack_pointer + 1
            else:
                needle_pointer = 0
                substring_length_found = 0
                if last_haystack_pointer != -1:
                    haystack_pointer = last_haystack_pointer + 1
                    last_haystack_pointer = -1
                else:
                    haystack_pointer = haystack_pointer  + 1
        
        return -1
                
                
          
            
        
        # brute force
#         first_characterin_needle = needle[0]
#         needle_length = len(needle)
        
#         haystackmap = {}
#         for index , haystackcharacter in enumerate(haystack):
#             if haystackcharacter ==  first_characterin_needle:
#                 haystackmap[index] = "" + haystackcharacter
        
#         for index in haystackmap:
#             substring1 = haystack[index : (index + needle_length)]
#             if substring1 == needle:
#                 return index
#         return -1
        
    
