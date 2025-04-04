# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

# Example 1:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4]
# Output: [2,7,4]
# Explanation: We return the node with value 2, colored in yellow in the diagram.
# The nodes coloured in blue are the deepest leaf-nodes of the tree.
# Note that nodes 6, 0, and 8 are also leaf nodes, but the depth of them is 2, but the depth of nodes 7 and 4 is 3.

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Helper function to perform DFS and return (depth, ancestor)
        def dfs(node, depth):
            if not node:
                return depth, None  # If node is None, return current depth and no ancestor

            # Recurse into left and right subtrees
            left_depth, left_ancestor = dfs(node.left, depth + 1)
            right_depth, right_ancestor = dfs(node.right, depth + 1)

            # If both subtrees have the same max depth, current node is LCA
            if left_depth == right_depth:
                return left_depth, node
            # If left subtree is deeper, return its ancestor
            elif left_depth > right_depth:
                return left_depth, left_ancestor
            # If right subtree is deeper, return its ancestor
            else:
                return right_depth, right_ancestor

        # Start DFS from the root at depth 0, return the LCA node
        return dfs(root, 0)[1]
