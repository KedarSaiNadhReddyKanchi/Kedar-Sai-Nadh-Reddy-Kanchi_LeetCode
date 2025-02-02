class Solution:
    def check(self, nums: List[int]) -> bool:

        # i need to find if the nums array is sorted pre rotation
        # if an array is rotated then it means the elements have been moved by certain positions. 

        # but since it is mentioned that the initially array is sorted in the ascending order
        
        # WHAT I WANT TO DO IS:
            # 1. Iterate over the given array and find the minimum value
                # but since it is mentioned that there can be duplicates
                # I need to make sure that the minimum value that I select should be the first occuring element
            # 2. now since I have the minimum element no matter what even if the array is rotated the sorted order is not disturbed.
                # so what i want to do is that I want to start iterating from the first occurence of the minimum element
                # and check if the ascending order is being maintained. 
                # and if not - then return False at that very point
        
        total_number_of_elements_in_the_array = len(nums) # size of the nums array
        minimum_element = min(nums) # find the minimum element
        first_occuring_index_of_the_minimum_element = None # find the first occurence of the minimum element

        # if the minimum element does not round up with multiple values like  - [3, 1, 1, 1, 1, 2] ==> [1, 1, 1, 1, 2, 3]
        for position , num in enumerate(nums):
            if num == minimum_element:
                first_occuring_index_of_the_minimum_element = position # found the first occurence of the minimum element
                break

        # but if the minimum element is being rounded up like [1, 1, 3, 2, 1, 1] ==> [1, 1, 1, 1, 2, 3]
        # then we need to find the first occurence of the second set of appereances
        if nums[0] == minimum_element and nums[total_number_of_elements_in_the_array - 1] == minimum_element:
            index = total_number_of_elements_in_the_array - 2
            while index >= 0:
                current_element = nums[index]
                if current_element == minimum_element:
                    index = index - 1
                else:
                    break
            first_occuring_index_of_the_minimum_element = index + 1

        # start the looop from the element after the first occurence of the minimum element
        start = first_occuring_index_of_the_minimum_element + 1

        previous_element = minimum_element

        # run the loop until it comes back to the first occurence of the minimum element
        while start != first_occuring_index_of_the_minimum_element:
            index = start
            if index >= total_number_of_elements_in_the_array:
                index = index - total_number_of_elements_in_the_array
            
            if index == first_occuring_index_of_the_minimum_element:
                break
            
            element_at_the_current_position = nums[index]
            if element_at_the_current_position >= previous_element:
                previous_element = element_at_the_current_position
                start = start + 1
            else:
                return False
        
        return True
            




        