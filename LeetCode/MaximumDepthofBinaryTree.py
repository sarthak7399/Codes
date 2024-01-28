# https://leetcode.com/problems/maximum-depth-of-binary-tree/?envType=study-plan-v2&envId=leetcode-75

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# Input: root = [3,9,20,null,null,15,7]
# Output: 3


from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if(root==None):
            return 0
        else:
            return max(self.maxDepth(root.left),self.maxDepth(root.right))+1