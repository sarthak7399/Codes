# https://leetcode.com/problems/find-bottom-left-tree-value/description/?envType=daily-question&envId=2024-02-28

# Example 2:
#     1
#    / \
#   2   3
#  /   / \
# 4   5   6
#      /
#     7
# Input: root = [1,2,3,4,null,5,6,null,null,7]
# Output: 7

# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bfs(self, root: Optional[TreeNode]) -> int:
        if not root: return -1
        queue = [(root, 0)]  # Initialize queue with root and its level
        max_level = (0, root.val)  # Initialize max_level with root's level and value

        while queue:
            node, level = queue.pop(0)
            if level > max_level[0]: max_level = (level, node.val)       # Update max_level if the current node is at a deeper level
            if node.left:  queue.append((node.left, level + 1))
            if node.right:  queue.append((node.right, level + 1))
        return max_level[1]

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        return self.bfs(root)