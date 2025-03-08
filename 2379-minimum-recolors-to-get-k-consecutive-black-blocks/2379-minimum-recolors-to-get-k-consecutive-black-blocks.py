class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        size = len(blocks)
        recolors = size
        whites = 0
        
        for right in range(size):
            if blocks[right] == "W":
                whites = whites + 1
            
            if right - left + 1 == k:
                recolors = min(recolors , whites)

                if blocks[left] == "W":
                    whites = whites - 1
                
                left = left + 1
        
        return recolors