class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        s_length = len(s)
        t_length = len(t)
        
        if s_length != t_length:
            return False
        
        mapping = {}
        mapped_characters_hashmap = {}
        
        for (char1 , char2) in zip(s, t):
            if char1 not in mapping:
                if char2 not in mapped_characters_hashmap:
                    mapping[char1] = char2
                    mapped_characters_hashmap[char2] = "already used in mapping to another character and therefore and cannot be used to map to another different character in s"
                else:
                    return False
            else:
                mapped_character = mapping[char1]
                if mapped_character == char2:
                    continue
                else:
                    return False
        
        return True
        
        