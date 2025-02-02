class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        
        groups = deque([])
        
        # to form the groups you need to first the sort the given array and check which groups they belong to
        new_nums = [[num , position] for position , num in enumerate(nums)]
        new_nums.sort()

        position_group_map = {}
        
        # now iterate and form the groups
        for num, position in new_nums:
            if len(groups) == 0:
                new_group = deque([num])
                groups.append(new_group)
            else:
                last_group = groups[-1]
                last_group_element = last_group[-1]
                difference = abs(num - last_group_element)
                if difference <= limit:
                    groups[-1].append(num)
                else:
                    new_group = deque([num])
                    groups.append(new_group)
            position_group_map[position] = len(groups)
        
        # since the iteration was done on a sorted nums array - the groups formed will by default be sorted as well.
        # print(groups)
        # print(position_group_map)

        # now you have the groups and the in which group each of the position is in. 
        # following that just fill in the values by popping out the values from the left of the each group
        for position, num in enumerate(nums):
            assigned_group = position_group_map[position]
            # least_possible_value_to_be_filled_at_this_point_from_the_respective_group is
            least_possible_value = groups[assigned_group - 1].popleft()
            nums[position] = least_possible_value
        
        return nums
