# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.inorderlist = []
    
    def recursivefunction(self, node):
        if node != None:
            self.recursivefunction(node.left)
            self. inorderlist.append(node.val)
            self.recursivefunction(node.right)
        
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self. recursivefunction(root)
        print(self.inorderlist)
        return self.inorderlist
    
        