# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def recursiveCall(self , node , val):
        if node is None:
            return
        elif node.val == val:
            return node
        
        found = self.recursiveCall(node.left , val)
        if found is not None:
            return found
        found = self.recursiveCall(node.right , val)
        if found is not None:
            return found
        return None
    
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if root == None:
            return None
        
        if root.val == val:
            return root

        found = self.recursiveCall(root , val)
        print(found)
        return found
        
        