"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if root is None:
            return root
        
        queue = []
        queue.append((root, 1))
        current_level = 1
        last_previous_node = None
        
        while queue:
            poppped_node, poppped_node_level = queue.pop(0)
            
            if poppped_node.left:
                queue.append((poppped_node.left , (poppped_node_level + 1)))
            
            if poppped_node.right:
                queue.append((poppped_node.right , (poppped_node_level + 1)))
                
            if current_level == poppped_node_level:
                print(f"node = {poppped_node.val} and poppped_level = {poppped_node_level}")
                if last_previous_node is not None:
                    last_previous_node.next = poppped_node
            else:
                print(f"node = {poppped_node.val} and poppped_level = {poppped_node_level} and current_level = {current_level}")
                current_level = poppped_node_level
                if last_previous_node is not None:
                    last_previous_node.next = None
            
            last_previous_node = poppped_node
        
        return (root)