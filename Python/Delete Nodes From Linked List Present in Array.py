# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/

# Example 1:
# Input: nums = [1,2,3], head = [1,2,3,4,5]
# Output: [4,5]
# Explanation:
# Remove the nodes with values 1, 2, and 3.

from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        s=set(nums)
        temp=head
        prev=ListNode(-1)
        temp2=prev
        while(temp is not None):
            if temp.val in s:                
                temp=temp.next                
            else:
                prev.next=temp
                temp=temp.next
                prev=prev.next
        else:
            prev.next=None   
        return temp2.next
                
        