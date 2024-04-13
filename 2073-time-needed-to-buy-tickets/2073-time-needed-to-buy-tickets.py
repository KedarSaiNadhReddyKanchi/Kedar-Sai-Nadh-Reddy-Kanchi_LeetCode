class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        tickets_needed_to_buy = tickets[k]
        time_count = 0
        
        while (tickets_needed_to_buy != 0):
            for position , perPersonTicketCount in enumerate(tickets):
                if perPersonTicketCount == 0:
                    continue
                else:
                    tickets[position] = perPersonTicketCount - 1
                    time_count = time_count + 1
                    if position == k:
                        tickets_needed_to_buy = tickets_needed_to_buy - 1
                        if tickets_needed_to_buy == 0:
                            break
            print(f"tickets = {tickets} and time_count = {time_count}")
        
        return time_count

        
                        
        