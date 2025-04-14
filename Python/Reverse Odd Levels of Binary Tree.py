# https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/

# Example 1:
# Input: root = [2,3,5,8,13,21,34]
# Output: [2,5,3,8,13,21,34]
# Explanation: 
# The tree has only one odd level.
# The nodes at level 1 are 3, 5 respectively, which are reversed and become 5, 3.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Reverse the values of nodes at odd levels in a binary tree.
        
        Args:
        root (TreeNode): The root of the binary tree.
        
        Returns:
        TreeNode: The root of the modified binary tree.
        """
        # Call the helper function to perform the reversal
        self.helper(root.left, root.right, 0)
        return root

    def helper(self, node1, node2, level):
        """
        Helper function to recursively traverse the tree and swap values 
        at odd levels.
        
        Args:
        node1 (TreeNode): Node from the left subtree.
        node2 (TreeNode): Node from the right subtree.
        level (int): Current level of the tree (0-based indexing).
        """
        # Base case: If either node is None, return
        if node1 is None or node2 is None:
            return

        # If the current level is odd, swap the values of the nodes
        if level % 2 == 0:
            node1.val, node2.val = node2.val, node1.val

        # Recur for the next level
        # Traverse opposite children to maintain the mirroring
        self.helper(node1.left, node2.right, level + 1)
        self.helper(node1.right, node2.left, level + 1)
