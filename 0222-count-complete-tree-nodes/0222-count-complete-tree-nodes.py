# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0
        
        queue = []
        queue.append(root)
        size = 1
        count = 0
        
        while size > 0:
            poppednode = queue.pop(0)
            size = size - 1
            count = count + 1
            
            if poppednode.left is not None:
                queue.append(poppednode.left)
                size = size + 1
            
            if poppednode.right is not None:
                queue.append(poppednode.right)
                size = size + 1
        
        return count
                
            
        