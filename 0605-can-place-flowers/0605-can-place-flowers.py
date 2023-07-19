class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        can_be_planted = 0
        prev = flowerbed[0]
        for pos in range(0,len(flowerbed)):
            
            if pos == 0:
                # that means there is no prev
                # then need to check the following position in the flowerbed
                if (pos + 1) != len(flowerbed):
                    if flowerbed[pos + 1] != 1 and flowerbed[pos] != 1:
                        can_be_planted = can_be_planted + 1
                        prev = 1
            
            elif prev == 1:
                prev = flowerbed[pos]
                continue
            
            else:
                if (pos + 1) != len(flowerbed):
                    if flowerbed[pos + 1] != 1 and flowerbed[pos] != 1:
                        can_be_planted = can_be_planted + 1
                        prev = 1
                    else:
                        prev = flowerbed[pos]
                else:
                    if flowerbed[pos] != 1:
                        can_be_planted = can_be_planted + 1
                        prev = 1

        if len(flowerbed) == 1 and flowerbed[0] == 0:
            can_be_planted = can_be_planted + 1

        # if flowerbed[0] == 0:
        #     if len(flowerbed) > 2 and flowerbed[1] == 0:
        #         can_be_planted = can_be_planted + 1
        #         print(can_be_planted)
        
        if can_be_planted >= n:
            return True
        else:
            return False




            # if prev == 1 and flowerbed[pos] == 1:
            #     return False
            # elif prev == 1 and flowerbed[pos] == 0 and flowerbed[pos + 1] == 1:
            #     continue