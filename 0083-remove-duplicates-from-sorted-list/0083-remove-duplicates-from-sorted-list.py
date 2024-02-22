# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None:
            return head
        
        startingNode = head.next
        previousNode = head
        
        while startingNode != None:
            if startingNode.val == previousNode.val:
                previousNode.next = startingNode.next
            else:
                previousNode = previousNode.next
            startingNode = startingNode.next
        
        return head
                
            