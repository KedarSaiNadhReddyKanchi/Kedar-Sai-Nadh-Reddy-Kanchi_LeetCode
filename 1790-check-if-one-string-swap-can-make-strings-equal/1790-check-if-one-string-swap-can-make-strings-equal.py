class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        changes = 0
        alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        s1_map = {character : 0 for character in alphabets}
        s2_map = {character : 0 for character in alphabets}

        first_index_of_difference = None
        second_index_difference = None
        # we only need to two differenct inidces of difference because
        # for 1 swap - we characters mis matching at two positions
        
        character_index = 0
        for character1 , character2 in zip(s1 , s2):
            if character1 == character2:
                changes = changes + 0
            else:
                changes = changes + 1

                if changes == 3:
                    return False

                if changes == 1:
                    first_index_of_difference = character_index
                
                if changes == 2:
                    second_index_difference = character_index
            
            s1_map[character1] = s1_map[character1] + 1
            s2_map[character2] = s2_map[character2] + 1
            character_index = character_index + 1
        
        if changes == 0:
            return True # no changes to be made in any one of the strings
        
        if second_index_difference is None:
            # then that means there is no second conflicting index
            # which cannot happen for a single swap to happen to make s1 = s2
            # and since the number of changes is not 0 then that means s1 != s2
            return False
        
        # now at this point we know that the number of changes is 2 - that mean 1 swap
        # and we know the indices at which we the characters were differing
        # we only be able to make a swap if the characters at the mismatching indices
        # are same appropriately
        condition_1 = s1[first_index_of_difference] == s2[second_index_difference]
        condition_2 = s1[second_index_difference] == s2[first_index_of_difference]
        resultant_condition = condition_1 and condition_2
        return resultant_condition

        # redundant code to check for the frequency matching
        # if characters differe in frequencies then we can return 0 
        # and if the characters do not differ in frequency then with changes = 2; 1 swap is possible
        for character1 , character2 in zip(s1 , s2):
            # now at this point it means that both the characters are present in each other
            # but now comapre frequencies if required but I do not think it would come to this point
            character_1_frequency = (s1_map[character1] == s2_map[character1])
            character_2_frequency = (s1_map[character2] == s2_map[character2])
            final_condition = (character_1_frequency and character_2_frequency)
            if not final_condition:
                # difference in frequencies so return False
                return False

        return True
