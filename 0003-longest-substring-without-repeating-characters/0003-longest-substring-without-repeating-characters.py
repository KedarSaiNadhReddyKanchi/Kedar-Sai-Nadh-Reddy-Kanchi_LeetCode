class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        character_list = list(s)
        hashMap = {}
        longest_substsring = []
        character_list_length = len(character_list)
        running_count = 0
        max_count = 0
        index = 0
        
        while index < character_list_length:
            character = character_list[index]
            if character not in hashMap:
                hashMap[character] = 1
                running_count = running_count + 1
                longest_substsring.append(character)
                if running_count > max_count:
                    max_count = running_count
                index = index + 1
            else:
                # if running_count > max_count:
                #     max_count = running_count
                removed_character = longest_substsring.pop(0)
                hashMap.pop(removed_character)
                # index = index - 1
                running_count = running_count - 1
        
        # print(longest_substsring)
        # print(max_count)
        return max_count