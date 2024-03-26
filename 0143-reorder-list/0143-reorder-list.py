# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        if head.next is None:
            return head
        
        hashmap = {}
        index = 1
        size = 0
        
        temp = head
        new_temp = head
        while temp is not None:
            temp = temp.next
            
            new_temp.next = None
            hashmap[index] = new_temp
            index = index + 1

            new_temp = temp
            size = size + 1
        
        # print(hashmap)
        # print(size)
        # print(head)
        
        start = 1
        end = size
        prev = None
        temp = head
        while start <= end:
            end_node = hashmap[end]
            start_node = hashmap[start]
            if prev is None:
                start_node.next = end_node
                prev = end
            else:
                prev_node = hashmap[prev]
                prev_node.next = start_node
                if start != end:
                    start_node.next = end_node
                prev = end
            
            start = start + 1
            end = end - 1
        
        # print(head)