class Solution(object):
    
    def updateLeastMid(self, least_possible_index , mid):
        if least_possible_index == -1:
            least_possible_index = mid
        else:
            if least_possible_index > mid:
                least_possible_index = mid
        return least_possible_index
    
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """

        pairs = []
        # for spell in spells:
        #     count = 0
        #     for potion in potions:
        #         if (spell * potion) >= success:
        #             count = count + 1
        #     pairs.append(count)
        # return pairs

        # in the potions list we need to find the least possible value that would make a successful pair 
        # so that the following values that come after the found least possible value would always be successful
        # and that is why we need to sort the potions array first

        potions.sort()
        sorted_potions_list = potions
        # print("sorted potions = ", sorted_potions)
        
        end_index = len(potions) - 1
        sorted_potions = {}
        
        for idx in range ( 0 , (end_index + 1)):
            sorted_potions[idx] = sorted_potions_list[idx]
        print("sorted potions = ", sorted_potions.values())
        
        
        for spell in spells:
            
            start = 0
            end = end_index
            least_possible_index = -1
            
            while (start <= end and start >= 0 and end <= end_index):
                # mid = start + int((end - start + 1) / 2)
                mid = int((end + start + 1) / 2)
                product = sorted_potions[mid] * spell
                
                if product >= success:
                    least_possible_index = self.updateLeastMid(least_possible_index , mid)
                    end = mid - 1
                
                elif product < success:
                    start = mid + 1
                
                else:
                    # if product == success
                    start = mid - 1
                    least_possible_index = self.updateLeastMid(least_possible_index , mid)
            
            if least_possible_index == -1:
                pairs.append(0)
            else:
                count = len(potions) - least_possible_index
                pairs.append(count)
        # print("sorted potions = ", sorted_potions)
        print("pairs = ", pairs)
        return pairs           


                    