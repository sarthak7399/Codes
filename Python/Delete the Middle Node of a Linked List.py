# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

# Example 1:
# Input: head = [1,3,4,7,1,2,6]
# Output: [1,3,4,1,2,6]
# Explanation:
# The above figure represents the given linked list. The indices of the nodes are written below.
# Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
# We return the new list after removing this node. 

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If the list is empty or contains only one node,
        # deleting the middle node results in an empty list
        if head is None or head.next is None:
            return None

        # Initialize slow and fast pointers
        slow_ptr = head
        fast_ptr = head

        # Keeps track of the node before slow_ptr
        prev = None

        # Move slow_ptr by 1 step and fast_ptr by 2 steps
        # When fast_ptr reaches the end, slow_ptr will be
        # pointing to the middle node
        while fast_ptr is not None and fast_ptr.next is not None:
            fast_ptr = fast_ptr.next.next   # Moves twice as fast
            prev = slow_ptr
            slow_ptr = slow_ptr.next

        # Remove the middle node by skipping it
        prev.next = slow_ptr.next

        # Return the head of the modified list
        return head