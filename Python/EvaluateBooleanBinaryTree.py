# https://leetcode.com/problems/evaluate-boolean-binary-tree/

# Example 1:
# Input: root = [2,1,3,null,null,0,1]
# Output: true
# Explanation: The above diagram illustrates the evaluation process.
# The AND node evaluates to False AND True = False.
# The OR node evaluates to True OR False = True.
# The root node evaluates to True, so we return true.

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def helper(self, root):
        if root.val == 0 or root.val == 1:
            return root.val == 1
        elif root.val == 2:
            return self.helper(root.left) or self.helper(root.right)
        elif root.val == 3:
            return self.helper(root.left) and self.helper(root.right)
        return False
        
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root)