class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        if len(word2) == 0 and len(word1) == 0:
            return ""

        if len(word1) == 0:
            return word2

        if len(word2) == 0:
            return word1

        pos = 0
        merged_string = ""
        while pos < len(word1):
            merged_string = merged_string + word1[pos:(pos + 1)]
            if pos < len(word2):
                merged_string = merged_string + word2[pos:(pos + 1)]
            pos = pos + 1

        if pos < len(word2):
            merged_string = merged_string + word2[pos:len(word2)]

        return merged_string
            


