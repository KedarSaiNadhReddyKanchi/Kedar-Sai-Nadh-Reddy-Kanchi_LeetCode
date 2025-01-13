class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        end = n + 1
        numbers = {num: True for num in range(0, end)}

        for num in nums:
            if num in numbers:
                del numbers[num]
        
        first_key = next(iter(numbers))
        return first_key
        