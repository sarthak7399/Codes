# https://leetcode.com/problems/leaf-similar-trees/description/?envType=study-plan-v2&envId=leetcode-75&__cf_chl_tk=HyYodGpGHXln3lCBwgSgMz5Mt5F17V1WwKfbVKqTu9I-1706898763-0-gaNycGzNElA

# Example 2:
# Input: root1 = [1,2,3], root2 = [1,3,2]
# Output: false

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# RECURSIVE SOLUTION
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def preorder(root, leaves):
            if not root.left and not root.right:
                leaves.append(root.val)
            if root.left: preorder(root.left, leaves)
            if root.right: preorder(root.right, leaves)
        
        leaves1, leaves2 = [], []
        preorder(root1, leaves1)
        preorder(root2, leaves2)
        return leaves1==leaves2


# ITERATIVE SOLUTION
# def iterInorder(root: Optional[TreeNode]) -> List:
#     res, st, curr = [], [], root
#     while curr or st:
#         while curr:
#             st.append(curr)
#             curr = curr.left
#         curr = st.pop()
#         if(curr.left==None and curr.right==None): res.append(curr.val)
#         # print(curr.val)  # Printing the value of the current node
#         curr = curr.right
#     return res

# class Solution:
#     def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:          
#         l1=iterInorder(root1)
#         l2=iterInorder(root2)
#         # print(l1,l2)
#         return l1==l2
