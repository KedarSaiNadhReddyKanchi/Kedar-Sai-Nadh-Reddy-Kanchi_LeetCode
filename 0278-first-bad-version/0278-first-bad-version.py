# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 1:
            if isBadVersion(n):
                return n
            else:
                return None
        
        if n == 2:
            if isBadVersion(n - 1):
                return 1
            else:
                return 2
        
        if n >= 3:
            if not isBadVersion(n - 1):
                return n
            
        start = 1
        end = n - 1
        result = 0
        
        while start <= end:
            mid = int((end + start) / 2)
            if isBadVersion(mid):
                result = mid
                end = mid - 1
            else:
                start = mid + 1
        return result
            
                
        