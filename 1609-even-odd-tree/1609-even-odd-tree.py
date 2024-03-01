# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        # creating an empty queue
        queue_temp = []
        
        # appending the root node to the empty queue at the beginning
        queue_temp.append((root , 0))
        
        # additional parameters required to complete this problem.
        previousValue = None
        currentLevel = 0
        flag = True
        
        # iterating over the queue until it is empty
        while ((len(queue_temp) != 0) and (flag != False)):
        
            # then pop out the top node from the queue as that has been visited or traversed
            # since we are appending the node along with the level we also get the level when pop
            node , level = queue_temp.pop(0)
            
            # printing out the current node at the top of the queue - level order traversal print
            print(f"level = {level} => node value = {node.val}")
            
            # now for the popped node we need to append the left child of the node to the queue
            # we need to append the left child first 
                # because it says that the level order traversal is from left to right
                # if it had said that the level order traversal is from right to left 
                    # then we would have appended the right child of the node to the queue first
                    # but since it is not we append the left child first and then the right child
            if node.left is not None:
                queue_temp.append((node.left , (level + 1)))
                
            # appening the right child of the node to the queue
            if node.right is not None:
                queue_temp.append((node.right , (level + 1)))
                
            # reset the previousValue to None when the level changes
            if (currentLevel != level):
                previousValue = None
                currentLevel = level
                
            # code to check whether the even-odd condition is being followed or not
            currentValue = node.val
            if (level % 2 == 0):
                if (currentValue % 2 == 1):
                    if previousValue is None:
                        previousValue = currentValue
                    else:
                        if (previousValue < currentValue):
                            previousValue = currentValue
                        else:
                            flag = False
                            break
                else:
                    flag = False
                    break
            
            else:
                if (level % 2 == 1):
                    if (currentValue % 2 == 0):
                        if previousValue is None:
                            previousValue = currentValue
                        else:
                            if (previousValue > currentValue):
                                previousValue = currentValue
                            else:
                                flag = False
                                break
                    else:
                        flag = False
                        break
                else:
                    flag = False
                    break

        print(flag)
        return flag
                
        