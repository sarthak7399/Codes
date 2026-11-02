# https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Example 1:
# Input: root = [4,8,5,0,1,null,6]
# Output: 5
# Explanation: 
# For the node with value 4: The average of its subtree is (4 + 8 + 5 + 0 + 1 + 6) / 6 = 24 / 6 = 4.
# For the node with value 5: The average of its subtree is (5 + 6) / 2 = 11 / 2 = 5.
# For the node with value 0: The average of its subtree is 0 / 1 = 0.
# For the node with value 1: The average of its subtree is 1 / 1 = 1.
# For the node with value 6: The average of its subtree is 6 / 1 = 6.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        # Count the number of nodes whose value equals
        # the average value of their subtree.
        answer = 0

        def dfs(node):
            # Allow the nested DFS function to update 'answer'.
            nonlocal answer

            # An empty subtree has sum 0 and contains 0 nodes.
            if node is None:
                return 0, 0

            # Recursively calculate the sum and node count
            # of the left subtree.
            left_sum, left_count = dfs(node.left)

            # Recursively calculate the sum and node count
            # of the right subtree.
            right_sum, right_count = dfs(node.right)

            # Calculate the total sum of the current subtree,
            # including the current node.
            total_sum = left_sum + right_sum + node.val

            # Calculate the total number of nodes in the current subtree.
            total_count = left_count + right_count + 1

            # Calculate the integer average of the subtree.
            # If it matches the current node's value, count this node.
            if node.val == total_sum // total_count:
                answer += 1

            # Return the subtree sum and node count to the parent.
            return total_sum, total_count

        # Start DFS from the root node.
        dfs(root)

        # Return the total number of matching nodes.
        return answer