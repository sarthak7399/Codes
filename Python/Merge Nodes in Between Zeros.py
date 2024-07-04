# https://leetcode.com/problems/merge-nodes-in-between-zeros/

# Example 1:
# Input: head = [0,3,1,0,4,5,2,0]
# Output: [4,11]
# Explanation: 
# The above figure represents the given linked list. The modified list contains
# - The sum of the nodes marked in green: 3 + 1 = 4.
# - The sum of the nodes marked in red: 4 + 5 + 2 = 11.

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # BASE CASE -> if we have a single zero, simply return null
        if not head.next:
            return None
        
        # fetch sum from current 0 to next 0
        ptr = head.next
        sum = 0
        while ptr.val != 0:
            sum += ptr.val
            ptr = ptr.next
        
        # assign sum on the first node between nodes having value 0
        head.next.val = sum
        
        # call and get the answer and connect the answer to next of head->next
        head.next.next = self.mergeNodes(ptr)
        
        # return head->next..=> new head
        return head.next