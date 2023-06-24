class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # left = []
        # left.append(1)
        # left_pos = 0

        # for num in nums:
        #         left.append(left[left_pos] * num)
        #         left_pos = left_pos + 1
        #         if len(left) == len(nums):
        #                 break
        # # print(left)

        # right = []
        # right.append(1)
        # right_pos = 0
        # pos  = len(nums) - 1
        # while pos > -1:
        #         right.append(right[right_pos] * nums[pos])
        #         right_pos = right_pos + 1
        #         pos = pos - 1
        #         if len(right) == len(nums):
        #                 break
        # # print(right)

        # start = 0
        # end = len(nums) - 1
        # result = []

        # while start < len(nums) and end >= 0:
        #         result.append(left[start] * right[end])
        #         start = start + 1
        #         end = end - 1
        # # print(result)
        # return result


  # algorithm that runs in O(n) time and without using the division operation.
        result = []
        result.append(1)
        result_pos = 0

        for num in nums:
                result.append(result[result_pos] * num)
                result_pos = result_pos + 1
                if len(result) == len(nums):
                        break
        #print(result)

        right = 1
        pos = len(nums) - 1
        while pos >= 0:
                result[pos] = result[pos] * right
                right = right * nums[pos]
                pos = pos - 1
        return (result)

