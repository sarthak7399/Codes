# https://leetcode.com/problems/same-tree/

# Example 1:
# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Example 2:
# Input: p = [1,2], q = [1,null,2]
# Output: false

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Method 1 : Iterative - Time Complexity O(N), Space Complexity O(N)
class Solution:
    def bfs(self, root: Optional[TreeNode]):
        queue = [root]  # Initialize the queue with the root node
        ans = []  # Initialize the list to store the values in BFS order
        while queue:
            curr = queue.pop(0)  # Dequeue the front element from the queue
            if curr is None:
                ans.append(None)  # Append None if the current node is None
            else:
                ans.append(curr.val)  # Append the value of the current node
                queue.append(curr.left)  # Enqueue the left child of the current node
                queue.append(curr.right)  # Enqueue the right child of the current node
        return ans

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Check if the lists obtained by BFS traversal of both trees are equal
        return self.bfs(p) == self.bfs(q)


# Method 2 : Recursive - Time Complexity O(N), Space Complexity O(N)
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Check if both p and q are None, indicating they are equal
        if not p and not q:
            return True
        
        # Check if either p or q is None, or if their values are not equal
        if not p or not q or p.val != q.val:
            return False
        
        # Recursively check if the left and right subtrees are equal
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))