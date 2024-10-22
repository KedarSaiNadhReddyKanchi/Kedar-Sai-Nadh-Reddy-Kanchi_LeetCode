class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # implement two pointer approach where you keep increasing the right pointer until you run out of buckets
        
        left = 0
        right = 0
        total_length = len(fruits)
        buckets = 2
        hashmap = {}
        
        max_count = 0
        running_count = 0
        
        first_fruit_type = None
        second_fruit_type = None
        
        while ((left < total_length) and (right < total_length)):
            left_value = fruits[left]
            
            if left_value not in hashmap:
                if buckets > 0:
                    hashmap[left_value] = 1
                    buckets = buckets - 1
                    running_count = running_count + 1
                    
                    if first_fruit_type == None:
                        first_fruit_type = left
                    else:
                        second_fruit_type = left
                        
                else:
                    print(f"left = {left} and right = {right} and running_count = {running_count}")
                    to_be_removed_value = fruits[first_fruit_type]
                    if running_count > max_count:
                        max_count = running_count
                    
                    del hashmap[to_be_removed_value]
                    right = second_fruit_type
                    first_fruit_type = right
                    # second_fruit_type = left
                    # hashmap[left_value] = 1
                    # running_count = running_count + 1
                    left = right
                    print(f"updated_left = {left}")
                    buckets = buckets + 1
                    
                    running_count = 1
                        
                    
            else:
                hashmap[left_value] = hashmap[left_value] + 1
                running_count = running_count + 1
            
            left = left + 1
            # print(f"moving_left = {left}")
            
        
        if running_count > max_count:
            max_count = running_count
        
        return (max_count)