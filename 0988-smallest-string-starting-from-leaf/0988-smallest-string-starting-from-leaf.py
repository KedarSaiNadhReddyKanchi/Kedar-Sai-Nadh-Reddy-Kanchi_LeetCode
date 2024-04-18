# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        hashmap = {
            0: 'a',
            1: 'b',
            2: 'c',
            3: 'd',
            4: 'e',
            5: 'f',
            6: 'g',
            7: 'h',
            8: 'i',
            9: 'j',
            10: 'k',
            11: 'l',
            12: 'm',
            13: 'n',
            14: 'o',
            15: 'p',
            16: 'q',
            17: 'r',
            18: 's',
            19: 't',
            20: 'u',
            21: 'v',
            22: 'w',
            23: 'x',
            24: 'y',
            25: 'z',
        }
        
        queue = deque()
        node_running_value = deque()
        node_running_value.appendleft(hashmap[root.val])
        
        queue.append((root , 1, node_running_value))
        # queue.append((root , 1, root.val))
        size = 1
        
        strings = []
        
        
        
        while size > 0:
            poppednode, level, stringvalue = queue.popleft()
            size = size - 1
            flag = False
            
            if poppednode is not None and poppednode.left is not None:
                # newstringvalue = (str)(poppednode.left.val) + (str)(stringvalue)
                new_string_value = deque(stringvalue)  # Create a copy of stringvalue
                new_string_value.appendleft(hashmap[poppednode.left.val])
                queue.append((poppednode.left , (level + 1), new_string_value))
                # flag = True
                size = size + 1
            
            if poppednode is not None and poppednode.right is not None:
                # newstringvalue = (str)(poppednode.right.val) + (str)(stringvalue)
                new_string_value = deque(stringvalue) 
                new_string_value.appendleft(hashmap[poppednode.right.val])
                queue.append((poppednode.right , (level + 1), new_string_value ))
                # stringvalue.popleft()
                size = size + 1
            
            if poppednode.left is None and poppednode.right is None:
                result_string = ''.join(map(str, stringvalue))
                strings.append(result_string)
        
        strings.sort()
        return strings[0]
                        
            
        