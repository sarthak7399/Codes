# https://leetcode.com/problems/add-one-row-to-tree/

# Example 1:
# Input: root = [4,2,6,3,1,5], val = 1, depth = 2
# Output: [4,1,1,2,null,null,6,3,1,5]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # Function to add nodes at the specified depth
    def add(self, root, val, depth, curr):
        # If root is None, return None
        if not root:
            return None
        
        # If current depth is equal to the target depth - 1
        if curr == depth - 1:
            # Store the left and right subtrees temporarily
            lTemp = root.left
            rTemp = root.right
            
            # Create new nodes with the given value
            root.left = TreeNode(val)
            root.right = TreeNode(val)
            
            # Reattach the original left and right subtrees to the new nodes
            root.left.left = lTemp
            root.right.right = rTemp
            
            return root
        
        # Recursively add nodes at the specified depth in the left and right subtrees
        root.left = self.add(root.left, val, depth, curr + 1)
        root.right = self.add(root.right, val, depth, curr + 1)
        
        return root

    # Main function to add a row of nodes at the specified depth
    def addOneRow(self, root, val, depth):
        # If depth is 1, create a new root with the given value
        if depth == 1:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot
        
        # Otherwise, call the helper function to add nodes at the specified depth
        return self.add(root, val, depth, 1)