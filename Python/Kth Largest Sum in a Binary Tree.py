# https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/

# Example 1:
# Input: root = [5,8,9,2,1,3,7,4,6], k = 2
# Output: 13
# Explanation: The level sums are the following:
# - Level 1: 5.
# - Level 2: 8 + 9 = 17.
# - Level 3: 2 + 1 + 3 + 7 = 13.
# - Level 4: 4 + 6 = 10.
# The 2nd largest level sum is 13.

from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthLargestLevelSum(self, root: TreeNode, k: int) -> int:
        res = []  # To store sum of each level
        q = deque([root])  # Queue for level-order traversal (BFS)

        while q:
            n = len(q)  # Number of nodes at the current level
            level_sum = 0  # Sum of node values at the current level
            
            for _ in range(n):
                node = q.popleft()
                level_sum += node.val
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            res.append(level_sum)  # Store the sum of the current level

        if k > len(res):
            return -1
        
        res.sort(reverse=True)  # Sort the level sums in descending order
        
        return res[k-1]  # Return the k-th largest sum