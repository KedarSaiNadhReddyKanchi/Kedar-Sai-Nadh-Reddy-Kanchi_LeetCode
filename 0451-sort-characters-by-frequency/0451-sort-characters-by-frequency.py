class Solution:
    def frequencySort(self, s: str) -> str:
        
        characterFrequency = {}
        numbermap = {}
        maxCount = 0
        
        for character in s:
            if character not in characterFrequency:
                characterFrequency[character] = 1
                if 1 not in numbermap:
                    numbermap[1] = {}
                numbermap[1][character] = True
                if maxCount < 1:
                    maxCount = 1
            else:
                current_character_count = characterFrequency[character]
                if current_character_count in numbermap:
                    if character in numbermap[current_character_count]:
                        del numbermap[current_character_count][character]
                
                new_character_count = current_character_count + 1
                if new_character_count not in numbermap:
                    numbermap[new_character_count] = {}
                numbermap[new_character_count][character] = True
                characterFrequency[character] = new_character_count
                if maxCount < new_character_count:
                    maxCount = new_character_count
        
        print(characterFrequency)
        print(numbermap)
        print(maxCount)
        
        sortedString = ""
        while (maxCount > 0):
            for key in numbermap[maxCount].keys():
                tempCount = maxCount
                while (tempCount > 0):
                    sortedString = sortedString + "" + key
                    tempCount = tempCount - 1
            maxCount = maxCount - 1
        
        print(sortedString)
        return sortedString
        