# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        if list == None and list2 == None:
            return None
        
        if list1 == None:
            return list2
        
        if list2 == None:
            return list1
        
        temp1 = list1
        temp2 = list2
        
        result = ListNode("dummy")
        result_head = result
        # print(result)
        
        while temp1 and temp2:
            
            if temp1.val <= temp2.val:
                temp1_temp = temp1.next
                temp1.next = None
                result.next = temp1
                result = result.next
                temp1 = temp1_temp
            else:
                temp2_temp = temp2.next
                temp2.next = None
                result.next = temp2
                result = result.next
                temp2 = temp2_temp
                
        if temp1 == None and temp2 != None:
            result.next = temp2
        
        elif temp1 != None and temp2 == None:
            result.next = temp1
        
        return result_head.next
                
                
                
        
