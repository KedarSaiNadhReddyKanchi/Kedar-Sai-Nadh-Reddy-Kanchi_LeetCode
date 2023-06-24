# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # ******************************using an additional data structure - list******************************
        # linked_list = []
        # temp = head

        # while temp != None:
        #     linked_list.append(temp.val)
        #     temp = temp.next

        # idx = len(linked_list) - 1
        # temp = head
        # while idx >= 0:
        #     temp.val = linked_list[idx]
        #     temp = temp.next
        #     idx = idx - 1

        # return head

        # ******************************no usage of an additional data structure ******************************
        # ****************************** ITERATIVE APPROACH ******************************

        # in this approach I need to maintain two pointers prev and next
        # prev so that the following node can point to it's previous node represented by prev
        # and next to iterate till the end of the linked list

        prev_node = None
        current_node = head
        next_node = None

        while current_node != None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        # print(prev_node)
        return prev_node



