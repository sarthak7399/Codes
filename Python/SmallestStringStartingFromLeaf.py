# https://leetcode.com/problems/smallest-string-starting-from-leaf/

# Example 1:
# Input: root = [0,1,2,3,4,3,4]
# Output: "dba"

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        result = []

        # Depth-first search function to traverse the tree and construct strings
        def dfs(node, path):
            # If node is None, return
            if not node:
                return
            
            # Append the character representing the current node's value to the path
            path.append(chr(97 + node.val))
            
            # If the current node is a leaf node, add the constructed string to the result list
            if not node.left and not node.right:
                result.append("".join(path[::-1]))
                path.pop()
                return
            
            # Recursively traverse the left and right subtrees
            dfs(node.left, path)
            dfs(node.right, path)
            
            # Remove the character representing the current node's value from the path
            path.pop()
        
        # Call the depth-first search function to construct strings
        dfs(root, [])
        
        # Sort the list of constructed strings lexicographically
        result.sort()
        
        # Return the lexicographically smallest string
        return result[0]
