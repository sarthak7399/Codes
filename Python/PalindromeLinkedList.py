# https://leetcode.com/problems/palindrome-linked-list/description/?envType=daily-question&envId=2024-03-15

# Example 1:
# Input: head = [1,2,2,1]
# Output: true

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # Helper function to reverse a linked list
    def reverse(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev

    # Main function to check if the linked list is a palindrome
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Initialize slow and fast pointers to find the middle of the list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the second half of the list
        rev = self.reverse(slow)
        
        # Compare the first half of the list with the reversed second half
        while rev:
            # If values don't match, the list is not a palindrome
            if head.val != rev.val:
                return False
            head = head.next
            rev = rev.next
        return True
