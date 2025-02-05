class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        changes = 0
        alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        s1_map = {character : 0 for character in alphabets}
        s2_map = {character : 0 for character in alphabets}
        
        for character1 , character2 in zip(s1 , s2):
            if character1 == character2:
                changes = changes + 0
            else:
                changes = changes + 1
                if changes == 3:
                    return False
            
            s1_map[character1] = s1_map[character1] + 1
            s2_map[character2] = s2_map[character2] + 1
        
        if changes == 0:
            return True # no changes to be made in any one of the strings
        
        for character1 , character2 in zip(s1 , s2):
            if character1 not in s2_map:
                # unknown character in s1 that is not there in s2 so return False
                return False
            
            if character2 not in s1_map:
                # unknown character in s2 that is not there in s1 so return False
                return False
            
            # now at this point it means that both the characters are present in each other
            # but now comapre frequencies if required but I do not think it would come to this point
            character_1_frequency = (s1_map[character1] == s2_map[character1])
            character_2_frequency = (s1_map[character2] == s2_map[character2])
            final_condition = (character_1_frequency and character_2_frequency)
            if not final_condition:
                # difference in frequencies so return False
                return False

        return True
