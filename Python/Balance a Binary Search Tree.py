# https://leetcode.com/problems/balance-a-binary-search-tree/

# Example 1:
# Input: root = [1,null,2,null,3,null,4,null,null]
# Output: [2,1,3,null,null,null,4]
# Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        if root is None : return None

        nodes = []

        def inorder(node) :
            if node is not None :
                inorder(node.left)
                nodes.append(node)
                inorder(node.right)

        inorder(root)

        def createBST(nodes, start, end) :
            if start > end : return None
            mid = start + (end-start)//2
            new_root = nodes[mid]
            new_root.left = createBST(nodes, start, mid-1)
            new_root.right = createBST(nodes, mid+1, end)
            return new_root

        return createBST(nodes, 0, len(nodes)-1)  