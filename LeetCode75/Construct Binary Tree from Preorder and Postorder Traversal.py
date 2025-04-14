# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/

# Example 1:
# Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
# Output: [1,2,3,4,5,6,7]

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # preorder = [root, left, right]
        # postorder = [left, right, root]

        def makeTree():            
            node = TreeNode(postorder.pop())  # Take the root from postorder (last element)

            # If the current node is not the next in preorder, construct the right subtree
            if node.val != preorder[-1]:  
                node.right = makeTree()  

            # If the current node is still not the next in preorder, construct the left subtree
            if node.val != preorder[-1]:  
                node.left = makeTree()  

            preorder.pop()  # Remove used root from preorder
            return node  

        return makeTree()  # Start tree construction from the root
