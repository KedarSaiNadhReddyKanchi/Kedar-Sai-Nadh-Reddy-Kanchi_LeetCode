# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        queue = deque()
        queue.append((root , 1 , "rootnode"))
        size = 1
        total = 0
        
        while size > 0:
            poppednode, level, typeofnode = queue.popleft()
            size = size - 1
            
            if poppednode.left is not None:
                queue.append((poppednode.left, (level + 1), "leftchildnode"))
                size = size + 1

            if poppednode.right is not None:
                queue.append((poppednode.right, (level + 1), "rightchildnode"))
                size = size + 1
                
            if poppednode.left is None and poppednode.right is None:
                if typeofnode == "leftchildnode":
                    total = total + poppednode.val
        
        return total
        