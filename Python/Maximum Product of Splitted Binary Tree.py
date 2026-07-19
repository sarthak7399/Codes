# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/

# Example 1:
# Input: root = [1,2,3,4,5,6]
# Output: 110
# Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        ans, total = -inf, 0  # ans stores maximum product, total will store total tree sum

        def dfs(root):
            nonlocal ans, total
            if not root:
                return 0  # Empty subtree has sum 0

            # Compute sum of current subtree
            Sum = root.val + dfs(root.left) + dfs(root.right)

            # Try splitting the tree here: one part = Sum, other = total - Sum
            ans = max(ans, (total - Sum) * Sum)

            return Sum  # Return subtree sum

        # First DFS to compute total sum of the tree
        total = dfs(root)

        # Second DFS to try all possible splits and update ans
        dfs(root)

        # Return result modulo 10^9 + 7
        return ans % (10**9 + 7)
