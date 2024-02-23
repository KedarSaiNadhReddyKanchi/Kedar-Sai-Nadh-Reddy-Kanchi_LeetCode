class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.hashmap = {}
        for position, num in enumerate(nums):
            self.hashmap[position] = num

    def sumRange(self, left: int, right: int) -> int:
        totalsum = 0
        for position in range(left , (right + 1)):
            totalsum = totalsum + self.hashmap[position]
        return totalsum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)