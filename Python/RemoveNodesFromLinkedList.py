# https://leetcode.com/problems/remove-nodes-from-linked-list/

# Example 1:
# Input: head = [5,2,13,3,8]
# Output: [13,8]
# Explanation: The nodes that should be removed are 5, 2 and 3.
# - Node 13 is to the right of node 5.
# - Node 13 is to the right of node 2.
# - Node 8 is to the right of node 3.

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize current node pointer
        current_node = head
        
        # Initialize stack to keep track of nodes to be kept
        stack = []
        
        # Iterate through the linked list
        while current_node:
            # Remove nodes from the stack that are smaller than the current node
            while stack and stack[-1].val < current_node.val:
                stack.pop()
            
            # Add the current node to the stack
            stack.append(current_node)
            
            # Move to the next node
            current_node = current_node.next
        
        # Initialize next node pointer
        next_node = None
        
        # Reconstruct the linked list from the stack
        while stack:
            current_node = stack.pop()
            current_node.next = next_node
            next_node = current_node
        
        # Return the head of the modified linked list
        return current_node
