class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
                    
        special_characters_hashmap = {
            "?" : 1,
            "!" : 1,
            "," : 1, 
            ";" : 1,
            "." : 1
        }
        
        if len(banned) == 0:
            first_index_of_space = paragraph.find(" ")
            if first_index_of_space == -1:
                last_character_of_the_sub_word = paragraph[-1]
                if last_character_of_the_sub_word in special_characters_hashmap:
                    paragraph = paragraph.rstrip(paragraph[-1])
                elif last_character_of_the_sub_word == "'" or last_character_of_the_sub_word == '"': 
                    paragraph = paragraph.rstrip(paragraph[-1])
                return paragraph.lower()
            else:
                return paragraph[0 : first_index_of_space].lower()
        else:
            hashmap = {}
            current_max = 0
            output_word = ""
            for word in banned:
                hashmap[word] = 0
            
            paragraph = paragraph.lower()
            start_point = 0
            space_index = 0
            unbanned_words = {}
            flag = False
            
            temp_word = []
            word = ""
            temp_word_length = 0
            for character in paragraph:
                if character in special_characters_hashmap or character == "'" or character == '"' or character == " ":
                    if temp_word_length > 0:
                        word = ''.join(temp_word)
                        temp_word = []
                        temp_word_length = 0
                        flag = True
                else:
                    temp_word.append(character)
                    temp_word_length = temp_word_length + 1
                    flag = False
                    
                if flag:
                    if word not in hashmap:
                        if word not in unbanned_words:
                            unbanned_words[word] = 1
                        else:
                            unbanned_words[word] = unbanned_words[word] + 1
                        
                        if current_max < unbanned_words[word]:
                            current_max = unbanned_words[word]
                            output_word = word
                    word = ""
                    flag = False
                            
                    
                
            if len(temp_word) > 0:
                word = ''.join(temp_word)
                temp_word = []
                if word not in hashmap:
                    if word not in unbanned_words:
                        unbanned_words[word] = 1
                    else:
                        unbanned_words[word] = unbanned_words[word] + 1
                        
                    if current_max < unbanned_words[word]:
                        current_max = unbanned_words[word]
                        output_word = word

            return output_word

        