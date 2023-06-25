class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        # s_strlist = list(s)
        s_hashMap = {}
        for char in s:
            if char in s_hashMap:
                s_hashMap[char] = s_hashMap[char] + 1
            else:
                s_hashMap[char] = 1
        # print(s_hashMap)
        
        for char in t:
            if char not in s_hashMap:
                return False
            else:
                if s_hashMap[char] > 0:
                    s_hashMap[char] = s_hashMap[char] - 1
                else:
                    return False
        
        for key in (s_hashMap):
            if s_hashMap[key] != 0:
                return False
        
        return True
        