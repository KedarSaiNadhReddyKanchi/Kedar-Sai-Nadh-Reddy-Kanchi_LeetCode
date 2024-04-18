# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        
        if depth == 1:
            newnode = TreeNode(val)
            newnode.left = root
            return newnode
        
        if depth == 2:
            firstnewnode = TreeNode(val)
            firstnewnode.left = root.left
            firstnewnode.right = None
            
            secondnewnode = TreeNode(val)
            secondnewnode.left = None
            secondnewnode.right = root.right
            
            root.left = None
            root.right = None
            
            root.left = firstnewnode
            root.right = secondnewnode
            
            return root
        
        queue = []
        queue.append((root , 1))
        size = 1
        
        previousLevelNodes = []
        
        while size > 0:
            poppednode , level = queue.pop()
            size = size - 1
            
            if level == (depth - 1):
                previousLevelNodes.append(poppednode)
                
            if poppednode is not None and poppednode.left is not None:
                queue.append((poppednode.left , (level + 1)))
                size = size + 1
            
            if poppednode is not None and poppednode.right is not None:
                queue.append((poppednode.right, (level + 1)))
                size = size + 1
        
        for eachnode in previousLevelNodes:
            firstnewnode = TreeNode(val)
            secondnewnode = TreeNode(val)
            
            firstnewnode.left = eachnode.left
            firstnewnode.right = None
            
            secondnewnode.left = None
            secondnewnode.right = eachnode.right
            
            eachnode.left = None
            eachnode.right = None
            
            eachnode.left = firstnewnode
            eachnode.right = secondnewnode
        
        print(root)
        
        return root
            
            
            
        
        