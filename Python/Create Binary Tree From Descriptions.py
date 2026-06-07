# https://leetcode.com/problems/create-binary-tree-from-descriptions/

# Example 1:
# Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
# Output: [50,20,80,15,17,19]
# Explanation: The root node is the node with value 50 since it has no parent.
# The resulting binary tree is shown in the diagram.

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> Optional[TreeNode]:

        # Recursively constructs the tree starting from a node value
        def construct_tree(cur_node_val):

            # Create current tree node
            new_node = TreeNode(cur_node_val)

            # Check if current node has children
            if cur_node_val in children_hashmap:

                # Create left subtree if left child exists
                if children_hashmap[cur_node_val][0] is not None:
                    new_node.left = construct_tree(
                        children_hashmap[cur_node_val][0]
                    )

                # Create right subtree if right child exists
                if children_hashmap[cur_node_val][1] is not None:
                    new_node.right = construct_tree(
                        children_hashmap[cur_node_val][1]
                    )

            return new_node

        # Stores all nodes that appear as children
        children_set = set()

        # Maps:
        # parent -> [left_child, right_child]
        children_hashmap: dict[int, list[int]] = {}

        # Build parent-child relationships
        for parent, child, isleft in descriptions:

            # Initialize parent entry if not present
            if parent not in children_hashmap:
                children_hashmap[parent] = [None, None]

            # Mark child node
            children_set.add(child)

            # Determine left (0) or right (1) position
            target = 0 if isleft else 1

            # Store child in correct position
            children_hashmap[parent][target] = child

        # Root is the node that never appears as a child
        for parent in children_hashmap:
            if parent not in children_set:
                head_node_val = parent
                break

        # Construct the entire tree from the root
        head = construct_tree(head_node_val)

        return head