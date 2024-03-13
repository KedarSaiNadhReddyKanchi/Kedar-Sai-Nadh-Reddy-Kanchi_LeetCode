class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap = {}
        evensum = 0
        oddsum = 0
        
        for character in s:
            if character not in hashmap:
                hashmap[character] = 1
                oddsum = oddsum + 1
            else:
                hashmap[character] = hashmap[character] + 1
                if ((hashmap[character]) % 2) == 0:
                    evensum = evensum + 2
                    oddsum = oddsum - 1
                else:
                    oddsum = oddsum + 1

        if oddsum > 0:
            return evensum + 1
        else:
            return evensum

        