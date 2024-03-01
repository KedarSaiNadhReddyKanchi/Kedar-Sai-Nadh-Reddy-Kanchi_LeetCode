# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def height(self, node):
        if node is None:
            return 0
        else:
            left_height = self.height(node.left)
            right_height = self.height(node.right)
            
            if left_height > right_height:
                return (left_height + 1)
            else:
                return (right_height + 1)
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.height(root)