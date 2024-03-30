# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/?envType=study-plan-v2&envId=leetcode-75&__cf_chl_tk=HyYodGpGHXln3lCBwgSgMz5Mt5F17V1WwKfbVKqTu9I-1706898763-0-gaNycGzNElA

# Example 1:
# Input: head = [5,4,2,1]
# Output: 6
# Explanation:
# Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
# There are no other nodes with twins in the linked list.
# Thus, the maximum twin sum of the linked list is 6. 

# Example 2:
# Input: head = [4,2,2,3]
# Output: 7
# Explanation:
# The nodes with twins present in this linked list are:
# - Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
# - Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
# Thus, the maximum twin sum of the linked list is max(7, 4) = 7. 


from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev= head, None
        while curr :
            forwardptr=curr.next
            curr.next=prev
            prev=curr
            curr=forwardptr
        return prev

    def pairSum(self, head: Optional[ListNode]) -> int:
        if head==None or head.next==None: return head
        slowptr,fastptr= head, head
        while fastptr and fastptr.next:
            slowptr=slowptr.next
            fastptr=fastptr.next.next
            
        secondhalf=self.reverseList(slowptr)

        total=float("-inf")
        while head and secondhalf:
            total=max(total,head.val+secondhalf.val)
            head=head.next
            secondhalf=secondhalf.next
        
        return total
