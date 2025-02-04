class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_map = {0 : 1}
        prefix_sum = 0
        count = 0
        for num in nums:
            prefix_sum = prefix_sum + num
            remainder = prefix_sum % k
            if remainder in prefix_map:
                count = count + prefix_map[remainder]
            
            if remainder not in prefix_map:
                prefix_map[remainder] = 1
            else:
                prefix_map[remainder] = prefix_map[remainder] + 1
        
        return count
