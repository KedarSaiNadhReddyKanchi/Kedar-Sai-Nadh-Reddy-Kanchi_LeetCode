class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        prev_num = nums[0]
        running_size = [1]
        size = len(nums)

        flag = None
        max_length = 1
        
        for position in range(1 , size):
            current_value = nums[position]
            if flag == None:
                if prev_num == current_value:
                    flag = None
                    running_size.append(1)
                    prev_num = current_value
                    continue

                if prev_num > current_value:
                    flag = "decreasing"
                elif prev_num < current_value:
                    flag = "increasing"
                
                last_size = running_size[-1]
                running_size.append(last_size + 1)
                prev_num = current_value
            else:
                if flag == "decreasing" and prev_num > current_value:
                    last_size = running_size[-1]
                    running_size.append(last_size + 1)
                    prev_num = current_value
                elif flag == "increasing" and prev_num < current_value:
                    last_size = running_size[-1]
                    running_size.append(last_size + 1)
                    prev_num = current_value
                else:
                    # there has been a break
                    if prev_num == current_value:
                        flag = None
                        running_size.append(1)
                        prev_num = current_value
                        continue

                    if prev_num > current_value:
                        flag = "decreasing"
                    elif prev_num < current_value:
                        flag = "increasing"
                    
                    running_size.append(2) # this time do not increase the length but intead set it 2 by default
                    prev_num = current_value
            
            max_length = max(max_length , running_size[-1])

        # print(running_size)
        return max_length

        