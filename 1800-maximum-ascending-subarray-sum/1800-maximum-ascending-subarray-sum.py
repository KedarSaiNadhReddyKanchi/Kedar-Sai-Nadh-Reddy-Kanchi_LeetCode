class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        running_sum = 0
        prev_num = 0
        max_ascending_subarray_sum = 0
        for num in nums:
            if num > prev_num:
                # ascending subarray starts from here
                running_sum = running_sum + num
                prev_num = num
            else:
                # ascending subarray sequence broken
                print("running sum of the ascending subarray up until this point = ", running_sum)
                max_ascending_subarray_sum = max(max_ascending_subarray_sum , running_sum)
                running_sum = num
                prev_num = num
        print("running sum of the ascending subarray up until this point = ", running_sum)
        max_ascending_subarray_sum = max(max_ascending_subarray_sum , running_sum)
        return max_ascending_subarray_sum


