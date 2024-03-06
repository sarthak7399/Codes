# https://leetcode.com/problems/linked-list-cycle/description/?envType=daily-question&envId=2024-03-06

# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# Example 2:
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                break
        else: return None
        
        slow = head
        while fast != slow:
            slow, fast = slow.next, fast.next
            
        return slow