# https://leetcode.com/problems/count-good-nodes-in-binary-tree/?envType=study-plan-v2&envId=leetcode-75

# Example 1:
# Input: root = [3,1,4,3,null,1,5]
# Output: 4
# Explanation: Nodes in blue are good.
# Root Node (3) is always a good node.
# Node 4 -> (3,4) is the maximum value in the path starting from the root.
# Node 5 -> (3,4,5) is the maximum value in the path
# Node 3 -> (3,1,3) is the maximum value in the path.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        count = 0
        stack = [(root, root.val)]  # Stack to store nodes and their corresponding maximum value
        
        while stack:
            node, max_val = stack.pop()     #Here, node gets assigned the first element of the popped tuple (which is a TreeNode), and max_val gets assigned the second element (which is the maximum value encountered so far).
            if node.val >= max_val:
                count += 1
            max_val = max(max_val, node.val)  # Update max_val for the next nodes
            
            if node.left:
                stack.append((node.left, max_val))
            if node.right:
                stack.append((node.right, max_val))
        return count
