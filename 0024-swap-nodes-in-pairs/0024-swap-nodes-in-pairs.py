# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return head
        
        temp = head
        prev = None
        count = 1
        flag = True
        prevswapnode = None
        
        while(temp.next is not None):
            prev = temp
            temp = temp.next
            count = count + 1
            if count == 2:
                if prevswapnode is None:
                    followingnode = temp.next
                    prev.next = followingnode
                    temp.next = prev
                    count = 0
                    prevswapnode = prev
                    if flag == True:
                        head = temp
                        flag = False
                        temp = prev
                    print(head)
                else:
                    print("intermediary print for else block")
                    print(prevswapnode)
                    followingnode = temp.next
                    prev.next = followingnode
                    temp.next = prev
                    count = 0
                    prevswapnode.next = temp
                    prevswapnode = prev
                    temp = prev
                    print(head)
        
        print(head)
        return head
        