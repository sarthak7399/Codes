# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Example 1:
# Input: head = [5,4,2,1]
# Output: 6
# Explanation:
# Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
# There are no other nodes with twins in the linked list.
# Thus, the maximum twin sum of the linked list is 6.


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize pointers for iterative reversal
        curr, prev = head, None

        while curr:

            # Store next node before breaking the link
            forwardptr = curr.next

            # Reverse the current node's pointer
            curr.next = prev

            # Move prev and curr one step forward
            prev = curr
            curr = forwardptr

        # prev becomes the new head of the reversed list
        return prev

    def pairSum(self, head: Optional[ListNode]) -> int:
        # Edge case: empty list or single node
        if head == None or head.next == None:
            return head

        # Find the middle of the linked list using
        # slow and fast pointer technique
        slowptr, fastptr = head, head

        while fastptr and fastptr.next:
            slowptr = slowptr.next
            fastptr = fastptr.next.next

        # Reverse the second half of the list
        secondhalf = self.reverseList(slowptr)

        # Store the maximum twin sum
        total = float("-inf")

        # Traverse first half and reversed second half together
        while head and secondhalf:

            # Update maximum twin sum
            total = max(total, head.val + secondhalf.val)

            # Move both pointers forward
            head = head.next
            secondhalf = secondhalf.next

        return total