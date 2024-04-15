# https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Example 2:
# Input: root = [4,9,0,5,1]
# Output: 1026
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # Initialize the answer to 0
        ans = 0
        # Define a depth-first search function
        def dfs(node, path: str):
            nonlocal ans  # Access the ans variable from the outer scope
            path = path + str(node.val)  # Append the current node value to the path
            if not node.left and not node.right:        # If the current node is a leaf node
                ans += int(path)  # Add the path value to the answer
            else:        
                if node.left:       # Recursively traverse the left subtree if it exists
                    dfs(node.left, path)                  
                if node.right:      # Recursively traverse the right subtree if it exists
                    dfs(node.right, path)        
        # Start the depth-first search from the root node with an empty path
        dfs(root, "")
        return ans
