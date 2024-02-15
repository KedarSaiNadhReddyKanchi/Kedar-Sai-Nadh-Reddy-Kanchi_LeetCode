class Solution:
    
    def checkIfPalindrome(self, wordCheck ):
        # get the length of the word
        wordLength = len(wordCheck)
        
        #initialize the head pointer
        headPointer = 0
        
        # initialize the tail pointer
        tailPointer = wordLength - 1
        
        #initialize a boolean flag
        isPalindrome = True
        
        # implement the loop to check if the word is a palindrome or not
        while ((headPointer <= tailPointer) and (isPalindrome == True)):
            if wordCheck[headPointer] == wordCheck[tailPointer]:
                headPointer = headPointer + 1
                tailPointer = tailPointer - 1
            else:
                isPalindrome = False
                
        return isPalindrome
    
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            returnedFlagValue = self.checkIfPalindrome(word)
            if returnedFlagValue == True:
                return word
            
        return ""
        