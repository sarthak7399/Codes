# https://leetcode.com/problems/reverse-linked-list/description/?envType=study-plan-v2&envId=leetcode-75

# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev= head, None
        while curr :
            forwardptr=curr.next
            curr.next=prev
            prev=curr
            curr=forwardptr
        return prev