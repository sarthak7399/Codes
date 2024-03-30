# https://leetcode.com/problems/reorder-list/description/?envType=daily-question&envId=2024-03-15

# Example 1:
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]

# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Check if the list is empty or has only one node
        if not head or not head.next:
            return
        
        # Find the middle of the list using the slow and fast pointers technique
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the second half of the list
        prev = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # Interleave nodes from the first and reversed second halves
        first_half = head
        second_half = prev
        while second_half.next:
            temp1 = first_half.next
            temp2 = second_half.next
            first_half.next = second_half
            second_half.next = temp1
            first_half = temp1
            second_half = temp2