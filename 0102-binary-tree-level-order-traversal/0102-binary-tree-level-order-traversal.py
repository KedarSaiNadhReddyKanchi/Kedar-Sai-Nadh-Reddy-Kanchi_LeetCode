# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return []
        
        queue = []
        queue.append((root , 1))
        total_list = []
        running_list = []
        current_level = 1
        
        while(len(queue) != 0 ):
            node , level = queue.pop(0)
            
            if current_level != level:
                total_list.append(running_list)
                current_level = level
                running_list = []

            running_list.append(node.val)
            
            if node.left is not None:
                queue.append((node.left , (level + 1)))
            
            if node.right is not None:
                queue.append((node.right , (level + 1)))
        
        if len(running_list) > 0:
            total_list.append(running_list)

        return total_list
            
            
            
        