class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
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
        while equal > 0:
            result[pointer] = pivot
            pointer = pointer + 1
            equal = equal - 1
        
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
