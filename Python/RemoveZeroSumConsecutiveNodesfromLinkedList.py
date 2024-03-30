# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/description/?envType=daily-question&envId=2024-03-12

# Example 1:
# Input: head = [1,2,-3,3,1]
# Output: [3,1]
# Note: The answer [1,2,1] would also be accepted.

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  # Create a dummy node to handle cases where the whole list is removed
        dummy.next = head  # Set the next of dummy node to the head of the list
        prefix_sum = 0  # Initialize a variable to keep track of prefix sum
        prefix_sums = {0: dummy}  # Create a dictionary to store prefix sums and corresponding nodes
        current = head  # Start from the head of the list

        while current:  # Loop through the list
            prefix_sum += current.val  # Update prefix sum
            if prefix_sum in prefix_sums:  # Check if the current prefix sum is already in the dictionary
                to_delete = prefix_sums[prefix_sum].next  # Get the node to delete
                temp_sum = prefix_sum + to_delete.val  # Calculate the prefix sum until the node to delete
                while to_delete != current:  # Loop until reaching the current node
                    del prefix_sums[temp_sum]  # Remove the prefix sum entry from the dictionary
                    to_delete = to_delete.next  # Move to the next node to delete
                    temp_sum += to_delete.val  # Update the temporary sum
                prefix_sums[prefix_sum].next = current.next  # Update the next pointer of the previous node
            else:  # If the prefix sum is not in the dictionary
                prefix_sums[prefix_sum] = current  # Add the prefix sum and node to the dictionary
            current = current.next  # Move to the next node

        return dummy.next  # Return the head of the updated list
