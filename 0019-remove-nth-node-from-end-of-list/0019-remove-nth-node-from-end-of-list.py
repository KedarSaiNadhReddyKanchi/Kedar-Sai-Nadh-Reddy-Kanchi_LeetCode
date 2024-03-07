# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        front = head
        temp = n - 1
        while temp > 0:
            front = front.next
            temp = temp - 1
        
        tail = head
        prev = None
        while front.next is not None:
            front = front.next
            prev = tail
            tail = tail.next
        
        if prev is not None:
            prev.next = tail.next
        else:
            head = head.next
        
        return head
        
        
        