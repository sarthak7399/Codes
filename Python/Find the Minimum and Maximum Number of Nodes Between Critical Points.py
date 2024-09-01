# https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/

# Example 2:
# Input: head = [5,3,1,2,5,1,2]
# Output: [1,3]
# Explanation: There are three critical points:
# - [5,3,1,2,5,1,2]: The third node is a local minima because 1 is less than 3 and 2.
# - [5,3,1,2,5,1,2]: The fifth node is a local maxima because 5 is greater than 2 and 1.
# - [5,3,1,2,5,1,2]: The sixth node is a local minima because 1 is less than 5 and 2.
# The minimum distance is between the fifth and the sixth node. minDistance = 6 - 5 = 1.
# The maximum distance is between the third and the sixth node. maxDistance = 6 - 3 = 3.

import math
from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        mind = math.inf
        prevc = None
        currc = None
        prev = head
        cur = head.next
        nex = cur.next
        firstc = None
        i = 1
        while(nex):
            if (nex.val > cur.val and prev.val > cur.val) or (nex.val < cur.val and prev.val < cur.val):
                if prevc == None:
                    firstc = i
                    prevc = i
                    currc = i
                else:
                    prevc = currc
                    currc = i
                    mind = min(mind,currc-prevc)
            i += 1
            prev = cur
            cur = nex
            nex = cur.next
            
        if mind == math.inf:
            return [-1,-1]
        return [mind,currc-firstc]