# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75

# Example 2:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root or root == p or root == q:      # If root is None or if either p or q is the root, return root
            return root
    
        # Recursively find the lowest common ancestor in the left subtree and right subtree
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
    
        if l and r:             # If both l and r are not None, it means p and q are found in different subtrees,
            return root         # and the current root is the lowest common ancestor
        
        return l or r           # If either l or r is not None, it means both p and q are found in the same subtree, and the lowest common ancestor is already determined
