# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        first_break_node = None
        last_break_node = None
        list2_temp = list2
        
        temp = list1
        first_position = 1
        
        while(first_position < a):
            temp = temp.next
            first_position = first_position + 1
            if (list2_temp.next is not None):
                list2_temp = list2_temp.next
        
        first_break_node = temp
        # print(first_break_node)
        
        second_position = first_position
        while (second_position <= b):
            temp = temp.next
            second_position = second_position + 1
            if (list2_temp.next is not None):
                list2_temp = list2_temp.next
        
        last_break_node = temp
        # print(last_break_node)
        
        first_break_node.next = list2
        
        while (list2_temp.next is not None):
            list2_temp = list2_temp.next
        
        list2_temp.next = last_break_node.next
        
        # print(list1)
        return list1