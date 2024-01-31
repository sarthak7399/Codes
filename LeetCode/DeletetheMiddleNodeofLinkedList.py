# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/?envType=study-plan-v2&envId=leetcode-75

# Input: head = [1,2,3,4]
# Output: [1,2,4]
# Explanation:
# The above figure represents the given linked list.
# For n = 4, node 2 with value 3 is the middle node.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        
        slow_ptr = head
        fast_ptr = head
        prev = None
        
        while fast_ptr is not None and fast_ptr.next is not None:
            fast_ptr = fast_ptr.next.next   #fast_ptr moves 2x speed as slow_ptr
            prev = slow_ptr
            slow_ptr = slow_ptr.next

        prev.next = slow_ptr.next

        return head
