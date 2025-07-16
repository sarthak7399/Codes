# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

# Example 1:
# Input: head = [1,0,1]
# Output: 5
# Explanation: (101) in base 2 = (5) in base 10

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# # Method 1 : Iterative - Time Complexity O(N), Space Complexity O(N)
# class Solution:
#     def getDecimalValue(self, head: Optional[ListNode]) -> int:
#         binary_string = ""
#         current = head
#         # Traverse the linked list and build a binary string
#         while current:
#             # Append the value of the current node (0 or 1) to the string
#             binary_string += str(current.val)
#             # Move to the next node
#             current = current.next
        
#         # Convert the binary string to an integer with base 2
#         # The '2' in int(binary_string, 2) specifies that the string is in base 2 (binary)
#         return int(binary_string, 2)
    

# Method 2 : Iterative - Time Complexity O(N), Space Complexity O(1)
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        result = 0
        current = head
        # Traverse the linked list
        while current:
            # Shift the current result one bit to the left (equivalent to multiplying by 2)
            # This makes space for the next bit from the linked list
            result = result << 1
            
            # Use bitwise OR to add the value of the current node (0 or 1)
            # This is like appending the new bit to the end of our number
            result = result | current.val
            
            # Move to the next node
            current = current.next
            
        return result