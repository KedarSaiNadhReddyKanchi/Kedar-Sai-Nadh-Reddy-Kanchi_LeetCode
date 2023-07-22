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
        
        # *************************************method 1*********************************
        # using a HASH MAP
        # hash_map = {}
        # temp = head
        # index = 0
        # while temp:
        #     if temp in hash_map:
        #         return True
        #     else:
        #         # here we are storing the node reference address as the key and value pair
        #         # this is because later on we can check if the same node reference number 
        #         #   has been hit up again in the cycle and if so return True
        #         hash_map[temp] = temp
        #     temp = temp.next
        # return False
        
        # *************************************method 2*********************************
        # using slow and fast pointers
        # the concept is that imagine that 
        #   the slow pointer moves 1 step forward at a time
        #   and the fast pointer moves 2 steps forward at a time
        # then if there is a cycle in the linked list then
        #   the slow and fast pointers will meet at one point of time
        # but if there is no cycle then the fast pointer will be the first to reach null node
        
        if head == None:
            return False
        
        slow = head
        fast = head
        
        
        while fast != None and fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
                
        return False
        
            
        
        