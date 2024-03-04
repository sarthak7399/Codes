# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/?envType=daily-question&envId=2024-03-03

# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:
# Input: head = [1], n = 1
# Output: []

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = self.findLength(head)
        i, traverseTill = 0, length - n - 1             # Find the index to traverse to remove the nth node from the end
        if traverseTill == -1:             # If the node to remove is the head node
            return head.next        
        curr = head            
        while i < traverseTill:      # Traverse the linked list to the node before the one to remove
            curr = curr.next
            i += 1
        
        curr.next = curr.next.next  # Remove the nth node from the end by updating pointers
        return head

    def findLength(self, head):
        count = 0
        if head is None: return count
        curr = head
        while curr is not None:
            count += 1
            curr = curr.next
        return count
