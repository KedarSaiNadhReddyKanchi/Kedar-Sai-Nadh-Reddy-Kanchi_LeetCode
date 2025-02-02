class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        frequency_map = {} # create a frequency map to store all the frequency of all the numbers in the list
        vacancy_map = {} # this map is to store the values that are being waited to be assigned to an existing subsequence

        # loop to initialize the frequency map
        for num in nums:
            if num not in frequency_map:
                frequency_map[num] = 0
            frequency_map[num] = frequency_map[num] + 1

        # now run a loop over the array across each element
        for num in nums:
            # retrieve the current frequency of the current element
            frequency = frequency_map[num]
            # if the current frequency = 0 then it means the element has already been visited or consumed into a subsequence

            # if the current frequency is > 0 then we need to assign a subsequence to this or create a new one 
            if frequency > 0:
                # check if the current value is being wanted by any existing subsequence
                if num in vacancy_map:
                    vacancy_map[num] = vacancy_map[num] - 1
                    frequency_map[num] = frequency_map[num] - 1
                    if vacancy_map[num] == 0:
                        del vacancy_map[num]
                    
                    # waiting for next element would be needed to added into the vacancy map
                    next_element = num + 1
                    if next_element not in vacancy_map:
                        vacancy_map[next_element] = 0
                    vacancy_map[next_element] = vacancy_map[next_element]  + 1
                
                else:
                    # if the element is not in the vacancy map -- then a new subsequence group needs to be created
                    # but the for the new subsequence group to be created we also the need the following 2 values 
                    # i.e. for num --> we need num + 1 and num + 2 values also to be present in the list to form a 
                        # valid subsequence group of minimum length == 3 and a consecutive increasing sequence
                    
                    next_value = num + 1
                    next_next_vaue = num + 1 + 1
                    
                    if next_value not in frequency_map or next_next_vaue not in frequency_map:
                        return False # cannot form a valid subsequence group without these values
                    
                    if frequency_map[next_value] == 0 or frequency_map[next_next_vaue] == 0:
                        return False # cannot form a valid subsequence group without these values
                    
                    # decrement the frequencies for all the three values as they have now been consumed into a group
                    frequency_map[num] = frequency_map[num] - 1
                    frequency_map[next_value] = frequency_map[next_value] - 1
                    frequency_map[next_next_vaue] = frequency_map[next_next_vaue] - 1
                    
                    # now again get the wait element and add it to the vacancy map
                    next_element = next_next_vaue + 1
                    if next_element not in vacancy_map:
                        vacancy_map[next_element] = 0
                    vacancy_map[next_element] = vacancy_map[next_element]  + 1
            
        return True 
