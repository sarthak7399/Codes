# https://leetcode.com/problems/maximal-score-after-applying-k-operations/

# Example 1:
# Input: nums = [10,10,10,10,10], k = 5
# Output: 50
# Explanation: Apply the operation to each array element exactly once. The final score is 10 + 10 + 10 + 10 + 10 = 50.

from heapq import heapify, heappop, heappush
from typing import List
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heapify(pq:=[-x for x in nums])
        score=0
        for i in range(k):
            x=-heappop(pq)
            score+=x
            if x==1:
                score+=k-1-i
                break
            heappush(pq, -((x+2)//3))
        return score
        