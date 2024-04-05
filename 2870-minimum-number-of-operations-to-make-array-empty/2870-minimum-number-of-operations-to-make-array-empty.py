class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = {}
        countone = {}
        total_count_of_numbers_in_countone = 0
        
        for num in nums:
            if num not in freq:
                freq[num] = 1
                countone[num] = 1
                total_count_of_numbers_in_countone = total_count_of_numbers_in_countone + 1
            else:
                freq[num] = freq[num] + 1
                if num in countone:
                    del countone[num]
                    total_count_of_numbers_in_countone = total_count_of_numbers_in_countone - 1
        
        if total_count_of_numbers_in_countone != 0:
            return -1
        
        total_deletion_operation_counts = 0
        
        for key in freq:
            value = freq[key]
            operationscount = 0
            
            if value % 3 == 0:
                number = (int)(value / 3)
                operationscount = operationscount + number
            
            elif value % 3 == 2:
                number_by_3 = (int)(value / 3)
                operationscount = operationscount + number_by_3 + 1
            
            elif value % 3 == 1:
                temp = value - 2
                temp_by_3 = (int)(temp / 3)
                operationscount = operationscount + temp_by_3 + 1 + 1
            
            total_deletion_operation_counts = total_deletion_operation_counts + operationscount

        return total_deletion_operation_counts
            