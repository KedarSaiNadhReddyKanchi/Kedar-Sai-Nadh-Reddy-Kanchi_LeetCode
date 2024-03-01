# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def recursive(self, node, preorderlist):
        if node is None:
            return
        
        preorderlist.append(node.val)
        self.recursive(node.left , preorderlist)
        self.recursive(node.right, preorderlist)
        
        return preorderlist
        
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.recursive(root , [])
        