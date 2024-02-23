class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashmap = {}
        for character in s:
            if character not in hashmap:
                hashmap[character] = 1
            else:
                hashmap[character] = hashmap[character] + 1
        
        for character in t:
            if character not in hashmap:
                return character
            else:
                if hashmap[character] == 0:
                    return character
                else:
                    hashmap[character] = hashmap[character] - 1
        