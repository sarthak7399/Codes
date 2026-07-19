# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

# Example 1:
# Input: root = [1,0,1,0,1,0,1]
# Output: 22
# Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs(self, node, currentNumber):
        # Base case: if node is None, no value to contribute
        if not node:
            return 0
        
        # Build binary number from root to current node
        # Shift previous bits left (multiply by 2)
        # then add current node value (0 or 1)
        currentNumber = currentNumber * 2 + node.val
        
        # If this is a leaf node (no children),
        # return the formed binary number
        if not node.left and not node.right:
            return currentNumber
        
        # Recursively compute sum from left subtree
        leftSum = self.dfs(node.left, currentNumber)
        
        # Recursively compute sum from right subtree
        rightSum = self.dfs(node.right, currentNumber)
        
        # Total sum contributed by this subtree
        return leftSum + rightSum
    
    def sumRootToLeaf(self, root):
        # Start DFS from root with initial number = 0
        return self.dfs(root, 0)