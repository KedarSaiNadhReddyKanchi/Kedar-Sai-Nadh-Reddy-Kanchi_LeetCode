class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        stolen_amount = [0 , 0] # chose to steal from this house , chose not to steal from this house
        while size > 0:
            popped_value = nums.pop()
            size = size - 1
            # so if I chose to steal from this house -- the max amount that I can steal from this point would be
                # amount to steal from this house + amount that can be stolen leaving the next adjacent house
            chose_this_house_to_steal = popped_value + stolen_amount[1]

            # not chose to this steal this house - then the maximum amount can be found 
            chose_not_to_steal_from_this_house = max(stolen_amount[0] , stolen_amount[1])

            # reset the stolen_amount for the next element
            stolen_amount = [chose_this_house_to_steal , chose_not_to_steal_from_this_house]
            print(f"for house with {popped_value} -- {stolen_amount}")

        return max(stolen_amount[0] , stolen_amount[1])