# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.tree_node_structures = {}
        self.duplicate_subtrees = {}

    def dfs(self, node):
        # perform preorder traversal
        if node is None:
            return [None]
        
        # mark the node as visited and maintain a list for the structure
        node_subtree_structure = [node.val]

        # go to the left subtree
        returned_left_substructure = self.dfs(node.left)

        # add the left substree to the node structure
        node_subtree_structure.extend(returned_left_substructure)

        # go to the right subtree
        returned_right_substructure = self.dfs(node.right)

        # add the right substree to the node structure
        node_subtree_structure.extend(returned_right_substructure)

        # convert the node structure into a immutable type to be used as a list - mostly string
        key_string = str(node_subtree_structure)

        # now before returning the node structure for this node
        # check if the same order exists in the visited node structures and if so add them to the list of duplicated
        if key_string in self.tree_node_structures:
            # duplicate strucute -- add it to the map of duplicate structures if not already
            if key_string not in self.duplicate_subtrees:
                # key as the structure and the value as the first value as the root node of that subtree
                self.duplicate_subtrees[key_string] = node
        else:
            # not a duplicate structure - so add it to the list of strucutres in the tree
            self.tree_node_structures[key_string] = node

        # now completely return the node structure from this node
        return node_subtree_structure

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.dfs(root)
        # print("self.tree_node_structures")
        # print(self.tree_node_structures)
        # print()
        # print("self.duplicate_subtrees")
        # print(self.duplicate_subtrees)

        # run over the pairs in the duplicate_subtrees and append all values into a list
        result = []
        for key in self.duplicate_subtrees:
            result.append(self.duplicate_subtrees[key])
        return result
        