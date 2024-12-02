# https://leetcode.com/problems/split-linked-list-in-parts/

# Example 1:
# Input: head = [1,2,3], k = 5
# Output: [[1],[2],[3],[],[]]
# Explanation:
# The first element output[0] has output[0].val = 1, output[0].next = null.
# The last element output[4] is null, but its string representation as a ListNode is [].

from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # First, count the length of the linked list
        curr, length = head, 0
        while curr:
            curr = curr.next
            length += 1
        # Determine the base size and the number of parts that will have an extra node
        base_size, extra_nodes = divmod(length, k)
        # Initialize the result array
        result = []
        curr = head

        # Split the list into parts
        for i in range(k):
            # Start a new part
            part_head = curr
            part_tail = None
            # Calculate the size of the current part
            part_size = base_size + (1 if extra_nodes > 0 else 0)
            if part_size > 0:
                # Move the current pointer to the end of the current part
                for _ in range(part_size - 1):
                    if curr:
                        curr = curr.next
                # Break the link to the next part
                if curr:
                    part_tail = curr
                    curr = curr.next
                    part_tail.next = None
            # Decrement the count of extra nodes
            if extra_nodes > 0:
                extra_nodes -= 1
            # Append the current part to the result
            result.append(part_head)
        return result