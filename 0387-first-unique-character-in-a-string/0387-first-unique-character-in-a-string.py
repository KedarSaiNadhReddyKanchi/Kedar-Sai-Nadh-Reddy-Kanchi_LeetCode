
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        hashmap = {}
        removed_hashmap = {}
        
        for index , character in enumerate(s):
            if character not in hashmap:
                if character not in removed_hashmap:
                    hashmap[character] = index
            else:
                del hashmap[character]
                removed_hashmap[character] = index
        # print(hashmap)
        result = None
        for new_s, new_val in hashmap.items():
            result = new_val
            break
        if result == None:
            return -1
        return result
        