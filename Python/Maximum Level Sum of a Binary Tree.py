# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

# Example 1:
# Input: root = [1,7,0,7,-8,null,null]
# Output: 2
# Explanation: 
# Level 1 sum = 1.
# Level 2 sum = 7 + 0 = 7.
# Level 3 sum = 7 + -8 = -1.
# So we return the level with the maximum sum which is level 2.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0  # If tree is empty

        # Queue for level order traversal
        q = [root]
        max_sum = float("-inf")  # Maximum level sum found so far
        max_level = 0            # Level having maximum sum
        level = 1                # Current level number

        # BFS traversal
        while q:
            level_sum = 0        # Sum of current level
            next_level = []      # Nodes of next level

            for node in q:
                level_sum += node.val  # Add current node value
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            # Update maximum sum and level if needed
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level

            # Move to next level
            q = next_level
            level += 1

        return max_level  # Return the level with maximum sum
