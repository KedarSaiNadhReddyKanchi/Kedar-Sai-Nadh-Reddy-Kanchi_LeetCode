class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix_map = {0: 1} # initially the prefix sum of 0 instance would be 1 i.e. completely before the 1st value
        count = 0
        prefix_sum = 0
        for num in nums:
            prefix_sum = prefix_sum + num
            to_be_removed_prefix = prefix_sum - k
            
            if to_be_removed_prefix in prefix_map:
                count = count + prefix_map[to_be_removed_prefix]
            
            if prefix_sum in prefix_map:
                prefix_map[prefix_sum] = prefix_map[prefix_sum] + 1
            else:
                prefix_map[prefix_sum] = 1

        return count
