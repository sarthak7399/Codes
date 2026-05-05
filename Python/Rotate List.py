# https://leetcode.com/problems/rotate-list/

# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # Edge case: empty list or single-node list
        
        if head is None or head.next is None:
            return head

        # Step 1: Find length of linked list and last node
        n = 1
        last = head
        while last.next is not None:
            n += 1
            last = last.next

        # Step 2: Reduce unnecessary rotations
        k = k % n

        # If no rotation needed
        if k == 0:
            return head

        # Step 3: Find the new tail
        # New tail will be at position (n-k)
        curr = head
        count = 1

        while curr is not None:
            if count == (n - k):
                break
            count += 1
            curr = curr.next

        # Step 4: New head is next node after new tail
        new = curr.next

        # Break the list at new tail
        curr.next = None

        # Step 5: Connect old tail to old head
        last.next = head

        # Return new head
        return new