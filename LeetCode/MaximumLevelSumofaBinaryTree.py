# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75&__cf_chl_tk=HyYodGpGHXln3lCBwgSgMz5Mt5F17V1WwKfbVKqTu9I-1706898763-0-gaNycGzNElA

# Example 1:
# Input: root = [1,7,0,7,-8,null,null]
# Output: 2
# Explanation: 
# Level 1 sum = 1.
# Level 2 sum = 7 + 0 = 7.
# Level 3 sum = 7 + -8 = -1.
# So we return the level with the maximum sum which is level 2.


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        q, max_sum, max_level, level = [root], float("-inf"), 0, 1
        while q:
            level_sum = 0
            next_level = []

            for node in q:
                level_sum += node.val
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level
            q = next_level
            level += 1
        return max_level