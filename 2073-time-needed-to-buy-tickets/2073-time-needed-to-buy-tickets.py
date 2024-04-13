class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        tickets_needed_to_buy = tickets[k]
        time_count = 0
        lesser_value_count = 0
        
        for position , ticketCount in enumerate(tickets):
            if ticketCount >= tickets_needed_to_buy:
                time_count = time_count + (tickets_needed_to_buy - 1)
            else:
                time_count = time_count + ticketCount
                if position < k:
                    lesser_value_count = lesser_value_count + 1
        
        print(f"time_count = {time_count} and lesser_value_count = {lesser_value_count}")
        total_time_count = time_count + 1 + k - lesser_value_count
        print(f"total_time_count = {total_time_count}")
        return total_time_count
                
        