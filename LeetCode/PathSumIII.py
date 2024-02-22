# https://leetcode.com/problems/path-sum-iii/description/?envType=study-plan-v2&envId=leetcode-75&__cf_chl_tk=HyYodGpGHXln3lCBwgSgMz5Mt5F17V1WwKfbVKqTu9I-1706898763-0-gaNycGzNElA

# Example 1:
#         10
#        /  \
#       5   -3
#      / \    \
#     3   2   11
#    / \   \
#   3  -2   1
# Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# Output: 3
# Explanation: The paths that sum to 8 are shown.

# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfsSum(self, root: Optional[TreeNode], targetSum: int, currSum: int) -> int:
        if not root:
            return 0

        # Count the number of paths starting from the current node
        count = 0
        if currSum + root.val == targetSum:
            count += 1

        # Recursively search for paths in the left and right subtrees
        count += self.dfsSum(root.left, targetSum, currSum + root.val)
        count += self.dfsSum(root.right, targetSum, currSum + root.val)

        return count

# FUNCTIONING OF dfsSum   
# For the root node 10, it checks if 10 equals the targetSum (8), which is false. It then recursively calls the dfsSum function on its left child (5) and right child (-3), passing the updated currSum as 10.
# For the left child 5, it checks if 10 + 5 equals the targetSum (8), which is false. It then recursively calls the dfsSum function on its left child (3) and right child (2), passing the updated currSum as 15.
# Similarly, it goes deeper into the tree, checking the sum at each node and updating the count accordingly.

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        # Count paths starting from the current node
        count = self.dfsSum(root, targetSum, 0)

        # Count paths starting from the left and right subtrees
        count += self.pathSum(root.left, targetSum)
        count += self.pathSum(root.right, targetSum)
        return count

# FUNCTIONING OF pathSum
# For the root node 10, it starts by calling self.dfsSum(root, targetSum, 0) to count paths starting from the current node.
# Then, it calls self.pathSum(root.left, targetSum) to count paths starting from the left subtree (5) and self.pathSum(root.right, targetSum) to count paths starting from the right subtree (-3).
# The recursion continues, exploring all possible paths in the tree and updating the count variable accordingly.