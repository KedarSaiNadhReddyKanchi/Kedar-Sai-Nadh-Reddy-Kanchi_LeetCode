class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        high = 0
        for num in candies:
            if num > high:
                high = num

        result = []
        for num in candies:
            if (num + extraCandies) >= high:
                result.append(True)
            else:
                result.append(False)
        
        return result