class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # either use pairs i , j and look for k with the help of a hashamp containing the latest indices of all the values
        # once you find a solution i , j , k --- then check if the same triplet is already present in the found set.
        # if so continue to check further by skipping this
        # if not we need to add it to the result - but before you add this to the solution
            # sort the solution i , j , k in ascending order and then add this 
            # this helps in basically adding duplicate triplet solutions irrespective of the order of the i , j , k
        
        # another way is below
        solution = []
        size = len(nums)

        # we sort the given array to make sure that the same number is not being checked with multiple times
        nums.sort() # if you do want to sort then you need to follow the above approach of using hashmap and all
        
        for position , num in enumerate(nums):
            if position > 0 and num == nums[position - 1]:
                # the starting value of the solution has already been visited in the previous iteration so skip this
                continue
            
            # now we will implement the 2-sum approach
            left = position + 1
            right = size - 1

            while left < right:
                left_value = nums[left]
                right_value = nums[right]
                three_sum = num + left_value + right_value

                if three_sum > 0:
                    # decrement the right pointer so that we can decrease the sum since the list has been sorted
                    right = right - 1 
                
                elif three_sum < 0:
                    # increment the left pointer so thar we increase the combination sum since the list has been sorted
                    left = left + 1 
                
                else:
                    # the threesum is no 0
                    # so add it to the solution
                    triplet = [num , left_value , right_value]
                    solution.append(triplet)

                    # now update the left pointer until 
                    # you reach a value that has not been previsouly visited as the second element in the combination
                    left = left + 1
                    while (left < right) and (nums[left] == nums[left - 1]):
                        left = left + 1
            
        return solution


            
