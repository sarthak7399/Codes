# https://leetcode.com/problems/binary-tree-right-side-view/description/?envType=study-plan-v2&envId=leetcode-75&__cf_chl_tk=HyYodGpGHXln3lCBwgSgMz5Mt5F17V1WwKfbVKqTu9I-1706898763-0-gaNycGzNElA

# Example 1:
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]

from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Method 1- RECURSION       
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        def printRight(root: TreeNode, level: int, result: List[int]):
            if not root: return
            if level == len(result): result.append(root.val)
            printRight(root.right, level + 1, result)
            printRight(root.left, level + 1, result)
        ans = []
        printRight(root, 0, ans)
        return ans

# METHOD 2- ITERATION
# class Solution:
#     def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
#         if not root: return []      # If the root is None, return an empty list
#         q, ans = [root], []     # Initialize a queue and a list to store the rightmost values
#         while q:        # Traverse the tree level by level using BFS
#             count = len(q)
#             for _ in range(count):
#                 curr = q.pop(0)        # Pop the first node from the queue                
#                 if not q: ans.append(curr.val)      # If this is the last node at the current level, add its value to the answer list
#                 if curr.right: q.append(curr.right)     # Add the right and left children of the current node to the queue
#                 if curr.left: q.append(curr.left)
#         return ans      # Return the list of rightmost values