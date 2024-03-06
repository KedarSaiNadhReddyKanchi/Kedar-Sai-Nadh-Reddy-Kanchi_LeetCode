class Solution:
    def minimumLength(self, s: str) -> int:
        
        end_string = ""
        starting_string = ""
        
        end_length = 0
        start_length = 0
        
        #pre_list = []
        #suff_list = []
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
                    #pre_list.append(starting_character)
                    last_starting_character = starting_character
                    start_length = start_length + 1
                    start_position = start_position + 1
                    
                    #suff_list.append(ending_character)
                    last_ending_character = ending_character
                    end_length = end_length + 1
                    end_position = end_position - 1
            else:                    
                flag = True
                
                #last_starting_character = pre_list[start_length - 1]
                if (last_starting_character == starting_character):
                    #pre_list.append(starting_character)
                    last_starting_character = starting_character
                    start_length = start_length + 1
                    start_position = start_position + 1
                    flag = False
                   
                #last_ending_character = suff_list[end_length - 1]
                if (last_ending_character == ending_character):
                    #suff_list.append(ending_character)
                    last_ending_character = ending_character
                    end_length = end_length + 1
                    end_position = end_position - 1
                    flag = False
                
                # (starting_character != last_starting_character) and (ending_character != last_ending_character)
                    
                if (flag == True):
                    #print(f"start_position = {start_position} and end_position = {end_position}")
                    #print("".join(suff_list))
                    s_list = s_list[start_position : (end_position + 1)]
                    #print("".join(s_list))
                    s_length = s_length - start_length - end_length
                    end_length = 0
                    start_length = 0
                    start_position = 0
                    end_position = s_length - 1
                    #pre_list = []
                    #suff_list = []
                
        
        s_length = s_length - start_length - end_length
        #print(f"s_length = {s_length}")
        #print(f"last_starting_character = {last_starting_character} and last_ending_character = {last_ending_character}")
        s_list = s_list[start_position : (end_position + 1)]
        #print(s_list)
        #print(s_list[0] == last_ending_character)
        
        if s_length == 1:
            if ((s_list[0] == last_ending_character) and (s_list[0] == last_starting_character)):
                s_length = 0
                start_length = 0
                end_length = 0
            else:
                start_length = 0
                end_length = 0
        
        # returned_value = 0
        # if start_length >= 0 and end_length >= 0:
        #     returned_value = s_length - start_length - end_length
        print(s_length)
        if s_length < 0:
            return 0
        return s_length
                        
                    
            
                
                
                
                
                
                
                
                
                
            