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
        # Store the minimum distance between consecutive critical points.
        mind = math.inf

        # Track the previous and current critical point indices.
        prevc = None
        currc = None

        # Use three pointers to examine each node along with
        # its previous and next nodes.
        prev = head
        cur = head.next
        nex = cur.next

        # Store the index of the first critical point.
        firstc = None

        # Index of the current node. The first possible critical point
        # is at index 1 because it needs both a previous and next node.
        i = 1

        while nex:
            # A node is a critical point if it is either:
            # 1. A local minimum: both neighbours are greater.
            # 2. A local maximum: both neighbours are smaller.
            if (
                (nex.val > cur.val and prev.val > cur.val)
                or
                (nex.val < cur.val and prev.val < cur.val)
            ):
                # Handle the first critical point.
                if prevc == None:
                    firstc = i
                    prevc = i
                    currc = i

                else:
                    # Move the current critical point to prevc
                    # and store the newly found point in currc.
                    prevc = currc
                    currc = i

                    # Calculate the distance between consecutive
                    # critical points and keep the minimum.
                    mind = min(mind, currc - prevc)

            # Move all three pointers one position forward.
            i += 1
            prev = cur
            cur = nex
            nex = cur.next

        # If fewer than two critical points were found, a valid
        # minimum and maximum distance cannot be calculated.
        if mind == math.inf:
            return [-1, -1]

        # mind = minimum distance between consecutive critical points.
        # currc - firstc = maximum distance between the first and last
        # critical points.
        return [mind, currc - firstc]