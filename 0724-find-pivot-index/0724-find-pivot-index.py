class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        # my initial solution is to first find the total sum of the give array
        total_sum = 0
        for num in nums:
            total_sum = total_sum + num
        
        # now to find the pivotal point, I will maintain two sums
        # one is left sum and one is the right sum

        # i will initialise the left_sum to 0 because for the first_element the left sum is 0
        left_sum = 0

        # now while looping the array from start to end
        # we will find out the right sum for a particular position using the below calculation
        # right sum = total sum - left sum - value at the position
        # lets for suppose the array [1,7,3,6,5,6]
        # while looping you are at value 7
        # so right sum = total sum(28) - left sum(1) - value at the position(7) = 20 = 3 + 6 + 5 + 6 as you see

        pivotal_point = 0
        for num in nums:
            right_sum = total_sum - left_sum - num
            if right_sum == left_sum:
                return pivotal_point
            left_sum = left_sum + num
            pivotal_point = pivotal_point + 1

        return -1
