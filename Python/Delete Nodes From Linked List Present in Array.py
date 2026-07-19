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
        """
        Removes all nodes from the linked list whose values are present in the given list 'nums'.
        
        Args:
            nums (List[int]): List of values to be removed.
            head (Optional[ListNode]): Head of the singly linked list.
        
        Returns:
            Optional[ListNode]: Modified linked list head (after removals).
        """
        
        # Step 1: Convert nums into a set for O(1) lookup time
        s = set(nums)

        # Step 2: Initialize pointers
        temp = head                  # To traverse the list
        prev = ListNode(-1)          # Dummy node before the new list starts
        temp2 = prev                 # Keep a reference to return final modified head

        # Step 3: Traverse the original linked list
        while temp is not None:
            # If current node's value is in 'nums', skip this node
            if temp.val in s:
                temp = temp.next
            else:
                # Otherwise, connect this node to the new list
                prev.next = temp
                temp = temp.next
                prev = prev.next
        else:
            # Step 4: Mark end of new list (avoid accidental links to old nodes)
            prev.next = None

        # Step 5: Return new head (next of dummy node)
        return temp2.next
        