# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.contaminated_binary_tree_values = set()
        print(root)
        self.levelOrderTraversal(root)
        print(self.contaminated_binary_tree_values)

    def levelOrderTraversal(self, root):
        # push in the root node
        if root is None:
            return
        
        correct_root_value = 0
        self.contaminated_binary_tree_values.add(0)

        queue = deque([])

        if root.left is not None:
            queue.append([root.left, "left child", 0])
        
        if root.right is not None:
            queue.append([root.right, "right child", 0])
        
        while queue:
            node_details = queue.popleft()

            current_node = node_details[0]
            current_node_value = current_node.val
            which_child = node_details[1] 
            parent_value = node_details[2]

            correct_node_value = None

            if which_child == "left child":
                correct_node_value = ((2 * parent_value) + 1)
                self.contaminated_binary_tree_values.add(correct_node_value)

            if which_child == "right child":
                correct_node_value = ((2 * parent_value) + 2)
                self.contaminated_binary_tree_values.add(correct_node_value)
            
            if current_node.left is not None:
                queue.append([current_node.left, "left child", correct_node_value])
            
            if current_node.right is not None:
                queue.append([current_node.right, "right child", correct_node_value])

    def find(self, target: int) -> bool:
        if target in self.contaminated_binary_tree_values:
            return True
        return False


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)