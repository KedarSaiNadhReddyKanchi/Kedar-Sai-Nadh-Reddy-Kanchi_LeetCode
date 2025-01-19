class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        total_sum_of_the_resulting_subarrays = 0
        # use the prefix sum logic

        prefix_sum = {}
        running_prefix_sum = 0
        for position, num in enumerate(nums):
            running_prefix_sum = running_prefix_sum + num
            prefix_sum[position] = running_prefix_sum
            start = max(0 , position - nums[position])
            if start == 0:
                subarray_sum = prefix_sum[position]
                total_sum_of_the_resulting_subarrays = total_sum_of_the_resulting_subarrays + subarray_sum
            else:
                subarray_sum = prefix_sum[position] - prefix_sum[start] + nums[start]
                total_sum_of_the_resulting_subarrays = total_sum_of_the_resulting_subarrays + subarray_sum
        
        return total_sum_of_the_resulting_subarrays