# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head == None:
            return None
        
        if head.next == None:
            return head
        
        if head and head.next and head.next.next == None:
            return head.next
        
        if head and head.next and head.next.next and head.next.next.next == None:
            return head.next
        
        
        temp = head.next.next.next
        mid = head.next
        
        first = 0
        second = 3
        midindex = 1
        
        while temp:
            mid_index = int((second - first + 1) / 2)
            if mid_index > midindex:
                mid = mid.next
                midindex = mid_index
            temp = temp.next
            second = second + 1
        
        print(mid.val)
        print(mid)
        return mid