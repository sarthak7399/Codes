# https://leetcode.com/problems/flip-equivalent-binary-trees/

# Example 1:
# Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
# Output: true
# Explanation: We flipped at nodes with values 1, 3, and 5.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flipEquiv(self, root1, root2):
        # Helper function to recursively check if two subtrees are flip equivalent
        def checker(node1, node2):
            # Base case: If both nodes are null, they are equivalent (empty trees)
            if not node1 and not node2:
                return True
            
            # If one node is null and the other isn't, or the values don't match, they are not equivalent
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            # Recursively check both possibilities:
            # 1. Children are not flipped: node1.left matches node2.left and node1.right matches node2.right
            # 2. Children are flipped: node1.left matches node2.right and node1.right matches node2.left
            return ((checker(node1.left, node2.left) or checker(node1.left, node2.right)) and
                    (checker(node1.right, node2.right) or checker(node1.right, node2.left)))

        # Call the helper function to compare the entire trees starting from the roots
        return checker(root1, root2)