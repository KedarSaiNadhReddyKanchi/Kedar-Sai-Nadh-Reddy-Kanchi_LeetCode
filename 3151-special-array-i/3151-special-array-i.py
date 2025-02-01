class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        current_parity = None
        for num in nums:
            remainder = num % 2
            parity = "even" if remainder == 0 else "odd"
            if current_parity == None:
                current_parity = parity
            else:
                if current_parity == parity:
                    return False
                current_parity = parity
        
        return True
        