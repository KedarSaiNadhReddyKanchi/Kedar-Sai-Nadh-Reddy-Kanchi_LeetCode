# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        queue = deque()
        queue.append((root , 1, 0))
        size = 1
        totalSum = 0
        
        while size > 0:
            poppednode, level, runningvalue = queue.popleft()
            size = size - 1
            
            if poppednode.left is not None:
                left_running_value = runningvalue * 10 + poppednode.val
                queue.append((poppednode.left, (level + 1), left_running_value))
                size = size + 1
            
            if poppednode.right is not None: 
                right_running_value = runningvalue * 10 + poppednode.val
                queue.append((poppednode.right, (level + 1), right_running_value))
                size = size + 1
                
            if poppednode.left is None and poppednode.right is None:
                current_running_value = runningvalue * 10 + poppednode.val
                totalSum = totalSum + current_running_value
    
        return totalSum
                
        
        