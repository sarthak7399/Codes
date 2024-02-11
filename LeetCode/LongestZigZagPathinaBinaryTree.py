# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/description/

# Example 1:
# Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
# Output: 3
# Explanation: Longest ZigZag path in blue nodes (right -> left -> right).

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right      

def maxZig(root, isLeft, depth):
    if root is None:
        return depth
    if isLeft:
        return max(maxZig(root.right, False, depth + 1), maxZig(root.left, True, 0))
    return max(maxZig(root.left, True, depth + 1), maxZig(root.right, False, 0))

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        return max(maxZig(root.left, True, 0), maxZig(root.right, False, 0))