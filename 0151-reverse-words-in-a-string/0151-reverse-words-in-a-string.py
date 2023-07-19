class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        form_word = ""
        words = []
        characters_in_the_word_formed = []
        for character in s:
            if character == " ":
                if len(characters_in_the_word_formed) > 0:
                    words.append(''.join(characters_in_the_word_formed))
                # form_word = ""
                characters_in_the_word_formed = []
            else:
                # form_word = form_word + character
                # i had to use a list to form the words from one space to another
                # because concatenation of a string using the '+' operator is a O(n) time complexity
                # so this within a loop of O(n) would make the whole loop to be O(n^2) time complexity
                # so append in the array
                characters_in_the_word_formed.append(character)

        # because after the last character is read
        # there is no space character coming in for the loop to execute the if condition within 
        # and append the formed word to the words list.
        # so after the loop has finished executing I have appended the last formed word to the list   
        # but again using the same condition as implemented in the if condition above
        # to not append any spaces as a word in to the words array.    
        if len(characters_in_the_word_formed) > 0:
            words.append(''.join(characters_in_the_word_formed))

        form_string = ""
        pos = (len(words) - 1)
        sentence = []
        while pos >= 0:
            if pos > 0:
                # form_string = form_string + words[pos] + " "
                sentence.append(words[pos])
                sentence.append(" ")
            else:
                # form_string = form_string + words[pos]
                sentence.append(words[pos])
            pos = pos - 1
        # since we are adding the space for joining the words in reverse
        # we need to remove the last trailing space as it should not be present.
        # form_string.strip()
        # return (form_string)
        return (''.join(sentence))

        