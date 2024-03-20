# https://leetcode.com/problems/merge-in-between-linked-lists/description/?envType=daily-question&envId=2024-03-15

# Example 1:
# Input: list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
# Output: [10,1,13,1000000,1000001,1000002,5]
# Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr = list1
        for _ in range(a - 1):  # Traverse list1 until reaching the position 'a'
            curr = curr.next        
        temphead = curr     # Store the node at position 'a' as temphead
        for _ in range(b - a + 2):  # Traverse list1 until reaching the position 'b'
            curr = curr.next   

        tempnext = curr     # Store the node after position 'b' as tempnext       
        temphead.next = list2   # Connect the end of list2 to the rest of list1 after position 'b'     
        while list2.next:   # Traverse list2 to find its last node
            list2 = list2.next
        list2.next = tempnext   # Connect the end of list2 to the node after position 'b' in list1
        return list1
