class Solution:
    def minimumLength(self, s: str) -> int:
        
        end_string = ""
        starting_string = ""
        
        end_length = 0
        start_length = 0
        
        last_starting_character = None
        last_ending_character = None
        
        s_list = list(s)
        s_length = len(s_list)
        
        start_position = 0
        end_position = s_length - 1
        
        while (start_position < end_position):
            starting_character = s_list[start_position]
            ending_character = s_list[end_position]
            
            if start_length == 0 and end_length == 0:
                if starting_character != ending_character:
                    break
                else:
                    last_starting_character = starting_character
                    start_length = start_length + 1
                    start_position = start_position + 1
                    
                    last_ending_character = ending_character
                    end_length = end_length + 1
                    end_position = end_position - 1
            else:                    
                flag = True
                
                if (last_starting_character == starting_character):
                    last_starting_character = starting_character
                    start_length = start_length + 1
                    start_position = start_position + 1
                    flag = False
                   
                if (last_ending_character == ending_character):
                    last_ending_character = ending_character
                    end_length = end_length + 1
                    end_position = end_position - 1
                    flag = False
                    
                if (flag == True):
                    s_list = s_list[start_position : (end_position + 1)]
                    s_length = s_length - start_length - end_length
                    end_length = 0
                    start_length = 0
                    start_position = 0
                    end_position = s_length - 1 
        
        s_length = s_length - start_length - end_length
        s_list = s_list[start_position : (end_position + 1)]
        
        if s_length == 1:
            if ((s_list[0] == last_ending_character) and (s_list[0] == last_starting_character)):
                s_length = 0
                start_length = 0
                end_length = 0
            else:
                start_length = 0
                end_length = 0

        print(s_length)
        if s_length < 0:
            return 0
        return s_length
                        
                    
            
                
                
                
                
                
                
                
                
                
            