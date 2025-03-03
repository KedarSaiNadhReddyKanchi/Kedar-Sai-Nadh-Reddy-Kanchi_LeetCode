class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # optimal one pass solution compared to the 2 pass solution described below
        nums_size = len(nums)
        left_pointer = 0
        right_pointer = nums_size - 1

        move_left = 0 
        move_right = nums_size - 1
        result = [None] * nums_size

        while (move_left < nums_size) and (move_right >= 0):
            left_value = nums[move_left]
            right_value = nums[move_right]

            # update the left portion of the result array 
            # with the sequential occurences of values less than the pivot
            # in the order they appear
            if left_value < pivot:
                result[left_pointer] = left_value
                # update the position for the left portion of the array
                # at which the next value should be placed
                left_pointer = left_pointer + 1
            
            # update the right portion of the result array 
            # with the sequential occurences of values greater than the pivot
            # in the order they appear from the right to left order
            if right_value > pivot:
                result[right_pointer] = right_value
                # update the position for the right portion of the array
                # at which the next value should be placed
                right_pointer = right_pointer - 1
            
            # update the move pointers that are moving across the nums array
            move_left = move_left + 1
            move_right = move_right - 1
        
        # now time to fill in all the values equal to the pivot that present in the nums array
        # this can be done by bridging any gap between the left_pointer and the right_pointer
        while left_pointer <= right_pointer:
            result[left_pointer] = pivot
            left_pointer = left_pointer + 1
        
        return result

        # MY SOLTUION WHICH GOT ACCEPTED BY WITH 2-PASS 
        # TIME COMPLEXITY NOT THAT GREAT

        less = 0
        greater = 0
        equal = 0
        size = 0
        for num in nums:
            size = size + 1
            if num == pivot:
                equal = equal + 1
            elif num < pivot:
                less = less + 1
            else:
                greater = greater + 1
        
        result = [None] * size
        pointer = less
        check = (equal == size)
        while equal > 0:
            result[pointer] = pivot
            pointer = pointer + 1
            equal = equal - 1
        
        if check:
            return result
        
        left = 0
        right = pointer

        for num in nums:
            if num < pivot:
                result[left] = num
                left = left + 1
            elif num > pivot:
                result[right] = num
                right = right + 1
        
        return result
