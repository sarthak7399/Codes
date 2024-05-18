# https://leetcode.com/problems/distribute-coins-in-binary-tree/

# Example 1:
# Input: root = [3,0,0]
# Output: 2
# Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(node, parent):
            if node is None:
                return 0            
            # Recursively distribute coins in the left and right subtrees
            moves = dfs(node.left, node) + dfs(node.right, node)            
            # Calculate the excess coins at this node (coins - 1)
            excess_coins = node.val - 1            
            # If there is a parent, pass the excess coins to the parent
            if parent is not None:
                parent.val += excess_coins            
            # Increment moves by the absolute value of excess coins
            moves += abs(excess_coins)            
            return moves        
        return dfs(root, None)
