class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        size = len(nums)
        position = size - 1
        right = position + k
        left = position - k
        total = 0

        while position >= 0:
            value_at_position = nums[position]
            right_value = None
            if right < size:
                right_value = nums[right]
            left_value = None
            if left >= 0:
                left_value = nums[left]
            
            if right_value is None and left_value is None:
                total = total + value_at_position
            elif left_value is not None and right_value is None and left_value < value_at_position:
                total = total + value_at_position
            elif left_value is None and right_value is not None and right_value < value_at_position:
                total = total + value_at_position
            elif left_value is not None and right_value is not None and left_value < value_at_position and right_value < value_at_position:
                total = total + value_at_position

            position = position - 1
            left = left - 1
            right = right - 1
            
        return total