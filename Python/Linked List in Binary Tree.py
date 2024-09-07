# https://leetcode.com/problems/linked-list-in-binary-tree/

# Example 1:
# Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
# Output: true
# Explanation: Nodes in blue form a subpath in the binary Tree.  


from collections import deque
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        d=deque()
        d.append(root)
        def dfs(node1,node2):
            if not node2:
                return True
            if not node1 or node1.val!=node2.val:
                return False
            return dfs(node1.right,node2.next) or dfs(node1.left,node2.next)
        while(d):
            for _ in range(len(d)):
                curr=d.popleft()
                if curr.val==head.val and dfs(curr,head):
                    return True
                if curr.left:
                    d.append(curr.left)
                if curr.right:
                    d.append(curr.right)
        return False
        