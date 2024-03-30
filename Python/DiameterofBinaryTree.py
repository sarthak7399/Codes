# https://leetcode.com/problems/diameter-of-binary-tree/description/?envType=daily-question&envId=2024-02-27

# Example 1:
#       1
#      / \
#     2   3
#    / \
#   4   5
# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Method 2: Time Complexity O(N), Space Complexity O(1)
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0
        def dfs(node):
            if not node: return 0
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            # Update diameter if the sum of left and right heights is greater
            self.diameter = max(self.diameter, left_height + right_height)
            return max(left_height, right_height) + 1   # Return the height of the current node's subtree 
        dfs(root)   # Start DFS from the root node
        return self.diameter

# Method 1: Time Complexity O(N), Space Complexity O(N)
# class Solution:
#     def dfsHeight(self, root: TreeNode) -> int:
#         if not root: return 0
#         left_height = self.dfsHeight(root.left)
#         right_height = self.dfsHeight(root.right)
#         # Return the height of the current node's subtree
#         return max(left_height, right_height) + 1       

#     def diameterOfBinaryTree(self, root: TreeNode) -> int:
#         if not root: return 0
#         # Calculate the height of the left and right subtrees
#         left_height = self.dfsHeight(root.left)
#         right_height = self.dfsHeight(root.right)

#         # Calculate the diameter passing through the current node
#         # It is the sum of the heights of the left and right subtrees
#         diameter = left_height + right_height

#         # Recursively find the diameter in the left and right subtrees
#         left_diameter = self.diameterOfBinaryTree(root.left)
#         right_diameter = self.diameterOfBinaryTree(root.right)

#         # Return the maximum of the current diameter and the diameters of left and right subtrees
#         return max(diameter, max(left_diameter, right_diameter))
    
