# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        if root is None:
            return []
        
        if root.left is None and root.right is None:
            if root.val == targetSum:
                return [[root.val]]
            return []
        
        queue = deque()
        queue.append((root, 1 , 0, []))
        size = 1
        result = []
        
        while size > 0:
            poppednode, level, runningvalue, elementslist = queue.popleft()
            size = size - 1
            print(f"poppednode = {poppednode.val} at level = {level} the runningvalue = {runningvalue} and elementslist = {elementslist}")
            
            if poppednode.left is not None:
                left_running_value = runningvalue + poppednode.val
                left_list = list(elementslist)
                left_list.append(poppednode.val)
                queue.append((poppednode.left , (level + 1), left_running_value, left_list))
                size = size + 1
                
            if poppednode.right is not None:
                right_running_value = runningvalue + poppednode.val
                right_list = list(elementslist)
                right_list.append(poppednode.val)
                queue.append((poppednode.right , (level + 1), right_running_value, right_list))
                size = size + 1
            
            if poppednode.left is None and poppednode.right is None:
                runningvalue = runningvalue + poppednode.val
                if runningvalue == targetSum:
                    elementslist.append(poppednode.val)
                    result.append(elementslist)
        
        print(result)
        return result
        