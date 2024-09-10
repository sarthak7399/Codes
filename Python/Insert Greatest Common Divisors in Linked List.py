# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

# Example 1:
# Input: head = [18,6,10,3]
# Output: [18,6,6,2,10,1,3]
# Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after inserting the new nodes (nodes in blue are the inserted nodes).
# - We insert the greatest common divisor of 18 and 6 = 6 between the 1st and the 2nd nodes.
# - We insert the greatest common divisor of 6 and 10 = 2 between the 2nd and the 3rd nodes.
# - We insert the greatest common divisor of 10 and 3 = 1 between the 3rd and the 4th nodes.
# There are no more adjacent nodes, so we return the linked list.

import math
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            gcd_val = math.gcd(curr.val, curr.next.val)
            gcd_node = ListNode(gcd_val)  # Create new node with the GCD
            gcd_node.next = curr.next     # Point new node to the next node
            curr.next = gcd_node          # Insert GCD node after current
            curr = gcd_node.next          # Move to the next pair
        return head