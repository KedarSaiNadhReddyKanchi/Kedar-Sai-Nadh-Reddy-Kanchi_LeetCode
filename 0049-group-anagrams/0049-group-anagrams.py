class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # check = "kedar"
        # checklist = list(check)
        # print(checklist)
        # checklist.sort()
        # print(checklist)
        # newcheck = "".join(checklist)
        # print(newcheck)
        # my logic is to reformat the words where all the characters are in sorted order
        # for that what i first did is to convert the word into a list
        # next i sorted the list of characters and then joined them back into word. 
        # this way all the anagrams will be of the same order
        
        new_list = []
        for word in strs:
            wordlist = list(word)
            wordlist.sort()
            new_list.append("".join(wordlist))
        
        print(new_list)
        
        hash_map = {}
        for item1, item2 in zip(strs, new_list):
            if item2 not in hash_map:
                hash_map[item2] = []
            hash_map[item2].append(item1)
        
        print(hash_map)
        
        final_list = []
        for value in hash_map.values():
            final_list.append(value)
        
        print(final_list)
        return final_list
                
        
        