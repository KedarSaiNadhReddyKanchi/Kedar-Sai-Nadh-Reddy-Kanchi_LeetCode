# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        hash_map = {}
        temp = head
        index = 0
        while temp:
            if temp in hash_map:
                return True
            else:
                hash_map[temp] = temp
            temp = temp.next
        return False
        
            
        
        